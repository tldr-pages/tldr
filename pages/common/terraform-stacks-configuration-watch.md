# terraform stacks configuration watch

> Watch the deployment progress of a Stack configuration version.
> See also: `terraform stacks configuration list`, `terraform stacks configuration fetch`, `terraform stacks configuration upload`.
> More information: [https://developer.hashicorp.com/terraform/cli/commands/stacks/configuration/watch](https://developer.hashicorp.com/terraform/cli/commands/stacks/configuration/watch).

- Watch a configuration by its ID:

`terraform stacks configuration watch -configuration-id {{configuration_id}}`

- Watch the latest configuration for a specific Stack:

`terraform stacks configuration watch -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`
