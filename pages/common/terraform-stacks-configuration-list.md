
# terraform stacks configuration list

> List the configuration versions for a Stack.
> See also: `terraform stacks configuration fetch`, `terraform stacks configuration upload`, `terraform stacks configuration watch`.
> More information: [https://developer.hashicorp.com/terraform/cli/commands/stacks/configuration/list](https://developer.hashicorp.com/terraform/cli/commands/stacks/configuration/list).

- List configurations for a Stack by organization, project, and Stack name:

`terraform stacks configuration list -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`

- List configurations for a Stack by ID, output as JSON:

`terraform stacks configuration list -stack-id {{stack_id}} -json`
