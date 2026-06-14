# agent-tester repl

> Start an interactive multi-model REPL to chat with multiple AI coding agents simultaneously.
> More information: <https://github.com/sroomberg/agenttester>.

- Start the REPL:

`agent-tester repl`

- Start with a named session to save and restore conversation history:

`agent-tester repl --session {{session_name}}`

- Start with a specific working directory for tool use and branch creation:

`agent-tester repl --workdir {{path/to/repo}}`

- Start with a custom configuration file:

`agent-tester repl --config {{path/to/config.yaml}}`

- Skip endpoint connection checks on startup:

`agent-tester repl --skip-checks`
