# terraform stacks

> Manage Terraform Stack configurations, deployments, and the lifecycle of a Stack.
> Some subcommands such as `init`, `validate`, `create`, `list`, `version`, `providers-lock`, `fmt`, and `configuration` have their own usage documentation.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/stacks>.

- Initialize a Stack's component configuration:

`terraform stacks init`

- Create a Stack in HCP Terraform:

`terraform stacks create -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`

- List Stacks in an organization:

`terraform stacks list -organization-name {{organization}}`

- Show the current Stacks plugin version:

`terraform stacks version`
