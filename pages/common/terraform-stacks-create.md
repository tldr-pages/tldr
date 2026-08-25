# terraform stacks create

> Create a new Stack in HCP Terraform.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/stacks/create>.

- Create a Stack by organization, project, and Stack name:

`terraform stacks create -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`

- Create a Stack with generated boilerplate configuration:

`terraform stacks create -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}} -with-template`
