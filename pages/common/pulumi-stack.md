# pulumi stack

> Manage stacks and view stack state.
> More information: <https://www.pulumi.com/docs/iac/cli/commands/pulumi_stack/>.

- Create a new stack:

`pulumi stack init {{stack_name}}`

- Show the stack state along with resource URNs:

`pulumi stack {{[-u|--show-urns]}}`

- List stacks in the current project:

`pulumi stack ls`

- List stacks across all projects:

`pulumi stack ls {{[-a|--all]}}`

- Select an active stack:

`pulumi stack select {{stack_name}}`

- Delete a stack:

`pulumi stack rm {{stack_name}}`

- Show stack outputs, including secrets, in plaintext:

`pulumi stack output --show-secrets`

- Export the stack state to a JSON file:

`pulumi stack export --file {{path/to/file.json}}`
