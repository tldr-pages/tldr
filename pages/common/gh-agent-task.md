# gh agent-task

> Manage GitHub agent tasks.
> More information: <https://cli.github.com/manual/gh_agent-task>.

- List the most recent agent tasks:

`gh {{[agent|agent-task]}} list`

- Create a new agent task for the current repository:

`gh {{[agent|agent-task]}} create "{{Improve the performance of the data processing pipeline}}"`

- Create a new agent task from a file:

`gh {{[agent|agent-task]}} create {{[-F|--from-file]}} {{path/to/file}}`

- View details about a specific agent task:

`gh {{[agent|agent-task]}} view {{session_id|pr_number|url|branch}}`

- Show the log of a specific agent task:

`gh {{[agent|agent-task]}} view --log {{session_id|pr_number|url|branch}}`
