# wlc

> Manage localization projects on a Weblate instance.
> More information: <https://docs.weblate.org/en/latest/wlc.html#commands>.

- List projects using a configuration file:

`wlc {{[-c|--config]}} {{path/to/file}} list-projects`

- List components in a project, and override API URL and API key:

`wlc {{[-u|--url]}} {{URL}} {{[-k|--key]}} {{key}} ls {{project}}`

- List translations from a component in a specific format:

`wlc {{[-f|--format]}} {{text|csv|json|html}} ls {{project}}/{{component}}`

- Print statistics for a project:

`wlc stats {{project}}`

- Display help:

`wlc {{[-h|--help]}}`
