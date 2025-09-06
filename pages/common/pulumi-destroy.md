# pulumi destroy

> Destroy all existing resources in a stack.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_destroy/>.

- Destroy all resources in the current stack:

`pulumi destroy`

- Destroy all resources in a specific stack:

`pulumi destroy {{[-s|--stack]}} {{stack}}`

- Automatically approve and destroy resources after previewing:

`pulumi destroy {{[-y|--yes]}}`

- Exclude protected resources from being destroyed:

`pulumi destroy --exclude-protected`

- Remove the stack and its configuration file after all resources in the stack are deleted:

`pulumi destroy --remove`

- Continue destroying the resources, even if an error is encountered:

`pulumi destroy --continue-on-error`
