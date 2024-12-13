## AWS Credentials

Configure your AWS Credentials

https://docs.aws.amazon.com/cli/v1/userguide/cli-configure-envvars.html

## Configure .env

Make a copy of `.env.example` called `.env` and update
the env vars for your desired use case.

Some example model id's you can use to set MODEL_ID:

### Anthropic Claude

- anthropic.claude-3-5-sonnet-20240620-v1:0

### Amazon Nova
- amazon.nova-pro-v1:0
- amazon.nova-lite-v1:0
- amazon.nova-micro-v1:0

### Command R
- cohere.command-r-plus-v1:0
- cohere.command-light-text-v14
- cohere.command-r-v1:0

## Getting Started

```sh
pip install -r requirements.txt
streamlit run app.py
```