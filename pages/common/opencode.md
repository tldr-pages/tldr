# opencode

> An AI coding agent.
> More information: <https://opencode.ai/docs/cli/>.

- Start the interactive TUI:

`opencode`

- Run opencode in non-interactive mode by passing a prompt directly:

`opencode run "{{message}}"`

- Use a specific model and agent:

`opencode run {{[-m|--model]}} {{provider}}/{{model}} --agent {{agent_name}} "{{message}}"`

- List all available models from configured providers:

`opencode models`

- Manage credentials and login for providers:

`opencode auth login`

- Start a headless opencode server for API access:

`opencode serve {{[-h|--hostname]}} {{hostname}} {{[-p|--port]}} {{port}}`

- Manage AI assistant agents for OpenCode:

`opencode agent {{command}}`

- Create a new agent with custom configuration:

`opencode agent create`
