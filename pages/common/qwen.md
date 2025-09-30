# qwen

> Launch an interactive prompt with Qwen3-Coder.
> See also: `gemini`.
> More information: <https://github.com/QwenLM/qwen-code>.

- Start a REPL session to chat interactively:

`qwen`

- Send the output of another command to Qwen and exit immediately:

`{{echo "Summarize the history of Rome"}} | qwen {{[-p|--prompt]}}`

- Override the default model (default: qwen3-coder-max):

`qwen {{[-m|--model]}} {{model_name}}`

- Run inside a sandbox container:

`qwen {{[-s|--sandbox]}}`

- Execute a prompt then stay in interactive mode:

`qwen {{[-i|--prompt-interactive]}} "{{Give me an example of recursion in Python}}"`

- Include all files in context:

`qwen {{[-a|--all-files]}}`

- Show memory usage in status bar:

`qwen --show-memory-usage`
