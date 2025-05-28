# codex

> Natural language code assistant for the terminal, powered by OpenAI.
> Reads and edits files in your current directory to fulfill requests.
> More information: <https://github.com/openai/codex>.

- Start an interactive Codex session in the current directory:

`codex`

- Run a single Codex command using a prompt:

`codex "{{your prompt}}"`

- Run a prompt with automatic approval of all file edits and commands:

`codex {{[-a|--approval-mode]}} full-auto "{{your prompt}}"`

- Use a specific provider and model:

`codex --provider {{provider_name}} {{[-m|--model]}} {{model_name}} "{{your prompt}}"`

- Load the entire repository as context (experimental):

`codex --full-context "{{your prompt}}"`

- Show the resource usage for the current session (run this command inside a session):

`/cost`

- Display help:

`codex --help`
