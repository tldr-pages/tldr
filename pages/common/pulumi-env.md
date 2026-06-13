# pulumi env

> Manage Pulumi environments.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_env/>.

- List all environments:

`pulumi env ls`

- Create an environment:

`pulumi env init {{environment_name}}`

- Set a value in an environment:

`pulumi env set {{environment_name}} {{key}} {{value}}`

- Edit an environment definition:

`pulumi env edit {{environment_name}}`

- Delete a value from an environment:

`pulumi env rm {{environment_name}} {{key}}`

- Delete an environment entirely:

`pulumi env rm {{environment_name}}`

- Display help:

`pulumi env {{[-h|--help]}}`
