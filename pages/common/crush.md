# crush

> AI-powered terminal assistant for software development tasks.
> Provides interactive chat interface with AI capabilities, code analysis, and LSP integration.
> More information: <https://github.com/charmbracelet/crush>.

- Start interactive mode:

`crush`

- Run with debug logging:

`crush {{[-d|--debug]}}`

- Run with debug logging in a specific directory:

`crush {{[-d|--debug]}} {{[-c|--cwd]}} {{path/to/project}}`

- Run a single non-interactive prompt:

`crush run "{{Explain the use of context in Go}}"`

- Run in dangerous mode (auto-accept all permissions):

`crush {{[-y|--yolo]}}`

- Display version:

`crush {{[-v|--version]}}`
