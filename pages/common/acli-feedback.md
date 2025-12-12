# acli feedback

> Submit a request or report a problem with Atlassian CLI.
> More information: <https://developer.atlassian.com/cloud/acli/reference/commands/feedback>.

- Display help:

`acli feedback {{[-h|--help]}}`

- Submit feedback with a summary and details:

`acli feedback {{[-s|--summary]}} "{{I have a problem}}" {{[-d|--details]}} "{{I have a problem with the acli}}" {{[-e|--email]}} "{{user@example.com}}"`

- Submit feedback with attachments:

`acli feedback {{[-s|--summary]}} "{{Bug report}}" {{[-a|--attachments]}} {{path/to/file1 path/to/file2 ...}}`

- Submit feedback with an estimated timeframe when the problem occurred:

`acli feedback {{[-s|--summary]}} "{{Issue description}}" {{[-t|--time]}} {{1h}}`
