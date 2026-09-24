# codex

> Natural language code assistant for the terminal, powered by OpenAI.
> Reads and edits files in your current directory to fulfill requests.
> More information: <https://developers.openai.com/codex/cli/reference>.

- Start an interactive Codex session in the current directory:

`codex`

- Run a single Codex command using a prompt:

`codex "{{prompt}}"`

- Run a prompt allowing Codex to edit files in the workspace:

`codex --sandbox workspace-write "{{prompt}}"`

- Use a specific model:

`codex {{[-m|--model]}} {{model_name}} "{{prompt}}"`

- Use a local open source model provider:

`codex --oss --local-provider {{lmstudio|ollama}} "{{prompt}}"`

- [Interactive] Display session configuration and token usage:

`/status`

- Display help:

`codex {{[-h|--help]}}`
