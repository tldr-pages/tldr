# terraform stacks

> Manage Terraform Stack configurations, deployments, and the lifecycle of a Stack.
> Some subcommands such as `init`, `validate`, `create`, `list`, `version`, `providers-lock`, `fmt`, and `configuration` have their own usage documentation.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/stacks>.

- Initialize a Stack's component configuration:

`terraform stacks init`

- Check whether the local component and deployment configurations are valid:

`terraform stacks validate`

- Create a Stack in HCP Terraform:

`terraform stacks create -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`

- List Stacks in an organization or project:

`terraform stacks list -organization-name {{organization}}`

- Retrieve warnings and errors for a stack configuration or deployment step:

`terraform stacks diagnostics -id {{stack_configuration_or_deployment_step_id}}`

- Show the current Stacks plugin version:

`terraform stacks version`

- Create or update the dependency lock file for the current component configuration:

`terraform stacks providers-lock`

- Format all configuration files in the current directory:

`terraform stacks fmt`
