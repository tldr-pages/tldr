# vllm

> Serve large language models efficiently and interact with them through an OpenAI-compatible API.
> More information: <https://docs.vllm.ai/en/latest/getting_started/quickstart.html>.

- Launch an OpenAI-compatible API server for a model:

`vllm serve {{model_name}}`

- Serve a model on a specific host and port:

`vllm serve {{model_name}} --host {{0.0.0.0}} --port {{8000}}`

- Start an interactive chat session:

`vllm chat`

- Run batch prompts from a file and write results to a file:

`vllm run-batch -i {{input.jsonl}} -o {{output.jsonl}} --model {{model_name}}`

- Print environment information for bug reports:

`vllm collect-env`

- List all available subcommands:

`vllm --help`
