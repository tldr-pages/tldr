# terraform stacks configuration upload

> Upload the deployment and component configuration files in the current directory to a Stack.
> See also: `terraform stacks configuration list`, `terraform stacks configuration fetch`, `terraform stacks configuration watch`.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/stacks/configuration/upload>.

- Upload configuration to a Stack by organization, project, and Stack name:

`terraform stacks configuration upload -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`

- Upload configuration to a Stack by ID:

`terraform stacks configuration upload -stack-id {{stack_id}}`

- Perform a speculative upload that will not trigger a deployment:

`terraform stacks configuration upload -stack-id {{stack_id}} -speculative`
