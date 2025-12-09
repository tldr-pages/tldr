# pulumi up

> Create or update the resources in a stack.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_up/>.

- Preview and deploy changes to a program and/or infrastructure:

`pulumi up`

- Automatically approve and perform the update after previewing it:

`pulumi up {{[-y|--yes]}}`

- Preview and deploy changes in a specific stack:

`pulumi up {{[-s|--stack]}} {{stack}}`

- Refresh the state of the stack's resources before updating:

`pulumi up {{[-r|--refresh]}}`

- Don't display stack outputs:

`pulumi up --suppress-outputs`

- Continue updating the resources, even if an error is encountered:

`pulumi up --continue-on-error`

- Display help:

`pulumi up {{[-h|--help]}}`
