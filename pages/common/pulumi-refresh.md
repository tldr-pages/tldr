# pulumi refresh

> Refresh the resources in a stack.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_refresh/>.

- Compare the current stack's state with the state in the cloud provider and adopt any changes into the current stack:

`pulumi refresh`

- Refresh resources in the current stack and show the operation as a rich diff:

`pulumi refresh --diff`

- Refresh resources in the current stack and return an error if any changes occur during the refresh:

`pulumi refresh --expect-no-changes`

- Only show a preview of the refresh, but don't perform the refresh itself:

`pulumi refresh --preview-only`

- The name of the stack to operate on (defaults to the current stack):

`pulumi refresh {{[-s|--stack]}} {{stack_name}}`

- Display help:

`pulumi refresh {{[-h|--help]}}`
