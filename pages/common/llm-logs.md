# llm logs

> View and manage logged prompt/response history.
> See also: `llm`.
> More information: <https://llm.datasette.io/en/stable/help.html>.

- Display the 3 most recent logged conversations:

`llm logs list`

- Display a specific number of recent logged conversations:

`llm logs list {{[-n|--count]}} {{10}}`

- Search logs for a specific term:

`llm logs list {{[-q|--query]}} "{{search_term}}"`

- Filter logs by a specific model:

`llm logs list {{[-m|--model]}} {{gpt-4o}}`

- Output logs in JSON format:

`llm logs list --json`

- Display the path to the logs database:

`llm logs path`

- Turn logging on or off globally:

`llm logs {{on|off}}`

- Display help:

`llm logs --help`
