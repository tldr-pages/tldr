# codex

> Natural language code assistant for the terminal, powered by OpenAI.
> Reads and edits files in your current directory to fulfill requests.
> More information: <https://github.com/openai/codex>.

- Start an interactive Codex session in the current directory:

`codex`

- Run a single Codex command using a prompt:

`codex "{{your prompt}}"`

- Run a prompt in full auto mode:

`codex --full-auto "{{your prompt}}"`

- Use a specific model:

`codex {{[-m|--model]}} {{model_name}} "{{your prompt}}"`

- Use a local open source model provider:

`codex --oss --local-provider {{lmstudio|ollama}} "{{your prompt}}"`

- [Interactive] Show the resource usage for the current session:

`/cost`

- Display help:

`codex {{[-h|--help]}}`
