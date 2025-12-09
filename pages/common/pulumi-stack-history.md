# pulumi stack history

> Display history for a stack.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack_history/>.

- Display history for the current stack:

`pulumi stack {{[hist|history]}}`

- Display history for the current stack showing full dates instead of relative dates:

`pulumi stack {{[hist|history]}} --full-dates`

- Display history for the current stack in JSON format:

`pulumi stack {{[hist|history]}} {{[-j|--json]}}`

- Display history for a specific stack:

`pulumi stack {{[hist|history]}} {{[-s|--stack]}} {{stack_name}}`

- Display help:

`pulumi stack {{[hist|history]}} {{[-h|--help]}}`
