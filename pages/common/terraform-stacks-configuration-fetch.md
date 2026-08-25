# terraform stacks configuration fetch

> Fetch the latest Stack configuration from a connected VCS repository.
> See also: `terraform stacks configuration list`, `terraform stacks configuration upload`, `terraform stacks configuration watch`.
> More information: [https://developer.hashicorp.com/terraform/cli/commands/stacks/configuration/fetch](https://developer.hashicorp.com/terraform/cli/commands/stacks/configuration/fetch).

- Fetch configuration for a Stack by organization, project, and Stack name:

`terraform stacks configuration fetch -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`

- Fetch configuration for a Stack by ID:

`terraform stacks configuration fetch -stack-id {{stack_id}}`

- Fetch configuration for a Stack by ID, output as JSON:

`terraform stacks configuration fetch -stack-id {{stack_id}} -json`
