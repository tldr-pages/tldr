opencode

>An AI coding agent with interactive terminal UI for intelligent coding assistance.
>Supports multiple AI providers including OpenAI, Anthropic Claude, Google Gemini, and more.
>More information: https://opencode.ai.


- Start opencode in interactive mode:

`opencode`

- Start opencode with a specific working directory:

`opencode --cwd {{path/to/project}}`

- Run a single prompt in non-interactive mode:

`opencode --prompt {{"Explain the use of context in Go"}}`

- Run a prompt and get output in JSON format:

`opencode --prompt {{prompt}} --output-format json`

- Start opencode with debug logging enabled:

`opencode --debug`

- Run a prompt quietly without the spinner (useful for scripts):

`opencode --prompt {{prompt}} --quiet`

- Display help information:

`opencode --help`

- Open command dialog (inside opencode TUI):

`Ctrl+K`

