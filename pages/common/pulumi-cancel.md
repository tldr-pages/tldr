# pulumi cancel

> Cancel a stack’s currently running update, if any.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_cancel/>.

- Cancel a stack’s currently running update, if any:

`pulumi cancel {{stack_name}}`

- Help for cancel:

`pulumi cancel --help`

- The name of the stack to operate on. Defaults to the current stack:

`pulumi cancel --stack {{stack_name}}`

- Skip confirmation prompts, and proceed with cancellation anyway:

`pulumi cancel --yes`
