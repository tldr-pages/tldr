# vibe

> Natural language code assistant for the terminal, powered by MistralAI.
> Reads and edits files in your current directory to fulfill requests.
> More information: <https://github.com/mistralai/mistral-vibe#usage>.

- Start an interactive Mistral Vibe session in the current directory:

`vibe`

- Resume the most recent Vibe session in the current directory:

`vibe {{[-c|--continue]}}`

- Start an interactive Vibe session to setup an API key then exit:

`vibe --setup`

- Run a single Vibe prompt in the terminal with automatic approval of file edits and commands:

`vibe --auto-approve {{[-p|--prompt]}} "{{your_prompt}}"`

- Run a single Vibe prompt in the terminal with the specified output format:

`vibe --ouput {{json, text, streaming}} {{[-p|--prompt]}} "{{your_prompt}}"`
