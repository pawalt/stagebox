import modal
import os
from dotenv import load_dotenv

load_dotenv()

secret = modal.Secret.from_dict({
    "ANTHROPIC_API_KEY": os.getenv("ANTHROPIC_API_KEY"),
})

app = modal.App.lookup("stagebox", create_if_missing=True)


image = modal.Image.debian_slim(
    python_version="3.12"
).apt_install(
    "nodejs",
    "npm",
).copy_local_file(
    "package.json",
    ".",
).copy_local_file(
    "package-lock.json",
    "."
).run_commands(
    "npm install",
    "npx playwright install-deps",
    "npm exec playwright install",
).copy_local_file(
    "index.mjs",
    "."
)

with modal.enable_output():
    sb = modal.Sandbox.create(
        image=image,
        secrets=[secret],
        app=app,
    )

p = sb.exec("npm", "start", stdout=modal.stream_type.StreamType.STDOUT, stderr=modal.stream_type.StreamType.STDOUT)
p.wait()
sb.terminate()