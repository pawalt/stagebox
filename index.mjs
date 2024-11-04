import { Stagehand } from "@browserbasehq/stagehand";
import { z } from "zod";

const stagehand = new Stagehand({
  env: "LOCAL",
  headless: true,
});

await stagehand.init({
    modelName: "claude-3-5-sonnet-latest",
});
await stagehand.page.goto("https://modal.com/docs");
await stagehand.act({ action: "click on guide" });
await stagehand.act({ action: "click on dynamic sandboxes" });
const codeObj = await stagehand.extract({
  instruction: "extract an example for exposing ports in a sandbox",
  schema: z.object({
    code: z.string(),
  }),
});
console.log(`The code for exposing ports is:
\`\`\`python
${codeObj.code}
\`\`\`
`);
