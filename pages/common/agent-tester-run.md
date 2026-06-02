# agent-tester run

> Run AI coding agents in parallel on a prompt and compare results.
> Each agent works in its own git worktree on a separate branch.
> More information: <https://github.com/sroomberg/agenttester>.

- Run all configured agents on a prompt:

`agent-tester run "{{prompt}}"`

- Run specific agents:

`agent-tester run --agents {{agent_name1,agent_name2}} "{{prompt}}"`

- Read the prompt from a file:

`agent-tester run --prompt-file {{path/to/prompt.txt}}`

- Run with a descriptive name for the branch and report:

`agent-tester run --name {{run_name}} "{{prompt}}"`

- Set a custom timeout for all agents:

`agent-tester run --timeout {{seconds}} "{{prompt}}"`

- Run against a specific git repository:

`agent-tester run --repo {{path/to/repo}} "{{prompt}}"`

- Push agent branches to a remote after the run:

`agent-tester run --push "{{prompt}}"`
