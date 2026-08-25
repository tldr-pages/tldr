# terraform stacks list

> List Stacks within a given organization or project.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/stacks/list>.

- List all Stacks in an organization:

`terraform stacks list -organization-name {{organization}}`

- List Stacks in a specific project within an organization:

`terraform stacks list -organization-name {{organization}} -project-name {{project}}`
