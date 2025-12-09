# zapier scaffold

> Add a starting trigger, create, search, or resource to an integration.
> More information: <https://platform.zapier.com/reference/cli#scaffold>.

- Scaffold a new trigger, create, search, or resource:

`zapier scaffold {{trigger|search|create|resource}} {{noun}}`

- Specify a custom destination directory for the scaffolded files:

`zapier scaffold {{trigger|search|create|resource}} {{noun}} {{[-d|--dest]}}={{path/to/directory}}`

- Overwrite existing files when scaffolding:

`zapier scaffold {{trigger|search|create|resource}} {{noun}} {{[-f|--force]}}`

- Exclude comments from the scaffolded files:

`zapier scaffold {{trigger|search|create|resource}} {{noun}} --no-help`

- Show extra debugging output:

`zapier scaffold {{[-d|--debug]}}`
