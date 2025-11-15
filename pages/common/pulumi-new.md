# pulumi new

> Create a new Pulumi project.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_new/>.

- Choose a template interactively:

`pulumi new`

- Create a project from a specific template (e.g `azure-python`):

`pulumi new {{provided-template}}`

- Create a project from a local file:

`pulumi new {{path/to/templates/aws-typescript}}`

- Create a project from a Git repository:

`pulumi new {{url}}`

- Use the specified secrets provider with the <pulumi.com> backend:

`pulumi new --secrets-provider {{passphrase}}`
