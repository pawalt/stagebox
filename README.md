# Stagebox

This is an example of using [Modal Sandboxes](https://modal.com/docs/guide/sandbox) to run the
[Stagehand](https://github.com/browserbase/stagehand) library to extract code from a web page.

## Running the example

1. Clone this repo
2. Set the `ANTHROPIC_API_KEY` environment variable in the `.env` file
3. Install the modal CLI and log in
4. `python sandbox.py`

Sadly this failed our simple test, but the infra works!

```
[stagehand:extraction] response: {"code":"{\n  \"sandbox\": {\n    \"ports\": [\n      {\n        \"containerPort\": 8080,\n        \"hostPort\": 8080,\n        \"protocol\": \"TCP\",\n        \"description\": \"Web application port\"\n      },\n      {\n        \"containerPort\": 443,\n        \"hostPort\": 443,\n        \"protocol\": \"TCP\",\n        \"description\": \"HTTPS port\"\n      }\n    ]\n  }\n}","metadata":{"progress":"Found complete example of port exposure in sandbox showing container-to-host port mapping (8080:8080 and 443:443) with TCP protocol and descriptions","completed":true}}
The code for exposing ports is:
```python
{
  "sandbox": {
    "ports": [
      {
        "containerPort": 8080,
        "hostPort": 8080,
        "protocol": "TCP",
        "description": "Web application port"
      },
      {
        "containerPort": 443,
        "hostPort": 443,
        "protocol": "TCP",
        "description": "HTTPS port"
      }
    ]
  }
}
```