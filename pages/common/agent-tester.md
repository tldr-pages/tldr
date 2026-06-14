# agent-tester

> Send a prompt to multiple AI coding agents in parallel and compare the results.
> See also: `agent-tester-run`, `agent-tester-repl`.
> More information: <https://github.com/sroomberg/agenttester>.

- Run all configured agents on a prompt:

`agent-tester run "{{prompt}}"`

- Start an interactive multi-model REPL:

`agent-tester repl`

- List available agents:

`agent-tester agents`

- List saved REPL sessions:

`agent-tester sessions`

- Resume a previous session:

`agent-tester --resume {{session_id}} repl`
