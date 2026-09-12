# llm models

> Manage models available to the `llm` command.
> More information: <https://llm.datasette.io/en/stable/help.html#llm-models-help>.

- List all available models:

`llm models list`

- List models matching a [q]uery string:

`llm models list {{[-q|--query]}} {{gpt}}`

- List models that support tools:

`llm models list --tools`

- List models along with their supported options:

`llm models list --options`

- Show the current default model:

`llm models default`

- Set the default model:

`llm models default {{model_id_or_alias}}`
