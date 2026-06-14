# vllmd task

> Run an agentic task with tool use against a vllmd-compatible endpoint.
> The model iterates with bash, file I/O, and git tools until the task is complete.
> More information: <https://github.com/sroomberg/vllmd>.

- Run a task against a local model:

`vllmd task "{{task_description}}" --endpoint {{http://localhost:port}} --model {{model_name}}`

- Run a task in a specific working directory:

`vllmd task "{{task_description}}" --endpoint {{http://localhost:port}} --model {{model_name}} --workdir {{path/to/repo}}`

- Set a custom maximum number of conversation turns:

`vllmd task "{{task_description}}" --endpoint {{http://localhost:port}} --model {{model_name}} --max-turns {{count}}`

- Use an SSH PEM key for authenticated git operations:

`vllmd task "{{task_description}}" --endpoint {{http://localhost:port}} --model {{model_name}} --pem {{path/to/key.pem}}`

- Override the default system prompt:

`vllmd task "{{task_description}}" --endpoint {{http://localhost:port}} --model {{model_name}} --system "{{system_prompt}}"`
