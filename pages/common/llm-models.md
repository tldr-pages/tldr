# llm models

> Manage and list available Large Language Models.
> See also: `llm`.
> More information: <https://llm.datasette.io/en/stable/help.html>.

- List all available models:

`llm models list`

- Search for models matching a keyword:

`llm models list {{[-q|--query]}} "{{search_term}}"`

- List models that support tool use:

`llm models list --tools`

- List models and show their available options:

`llm models list --options`

- Display the current default model:

`llm models default`

- Set a default model:

`llm models default {{gpt-4o}}`

- Display help:

`llm models --help`
