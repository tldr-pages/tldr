# pulumi plugin

> Manage language and resource provider plugins manually.
> Other commands manage these automatically.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_plugin/>.

- List all plugins on the downloaded cache:

`pulumi plugin ls`

- List plugins being used by the current project in JSON format:

`pulumi plugin {{[-p|--project]}} {{[-j|--json]}}`

- Install a plugin kind (e.g resource) with the latest version or a specific one:

`pulumi plugin install {{kind}} {{name}} {{version}}`

- Remove a plugin kind (e.g. resource) and interactively pick a version or provide a specific one:

`pulumi plugin rm {{kind}} {{name}} {{version}}`

- Display help:

`pulumi plugin {{[-h|--help]}}`
