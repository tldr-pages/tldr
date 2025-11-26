# cline

> AI-powered autonomous coding agent CLI for creating, editing files, and executing commands.
> Supports multiple AI providers including Anthropic, OpenAI, Google Gemini, and more.
> More information: <https://docs.cline.bot/cline-cli/overview>.

- Authenticate with an AI provider:

`cline auth`

- Start a new coding task:

`cline task {{task_description}}`

- Start a task in a specific workspace directory:

`cline task {{task_description}} --workspace {{path/to/directory}}`

- List all running Cline instances:

`cline instance list`

- Stop a running instance:

`cline instance stop {{instance_id}}`

- View configuration settings:

`cline config`

- Display version information:

`cline --version`

- Display help for a specific command:

`cline {{command}} --help`
