# llm logs

> Explore prompts and responses logged to an SQLite database by the `llm` command.
> More information: <https://llm.datasette.io/en/stable/help.html#llm-logs-help>.

- Show the most recent logged prompts and their responses (3 by default):

`llm logs list`

- Show the [n] most recent entries:

`llm logs list {{[-n|--count]}} {{10}}`

- Search logged prompts and responses for a [q]uery string:

`llm logs list {{[-q|--query]}} {{query}}`

- Show the current status of database logging:

`llm logs status`

- Turn off logging for all prompts:

`llm logs off`

- Turn logging back on:

`llm logs on`

- Print the path to the `logs.db` database file:

`llm logs path`

- Back up the logs database to a file:

`llm logs backup {{path/to/backup.db}}`
