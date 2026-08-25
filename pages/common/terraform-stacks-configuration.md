
# terraform stacks configuration

> Manage Stack configurations: list, upload, fetch, and watch.
> Some subcommands such as `list`, `upload`, `fetch`, and `watch` have their own usage documentation.
> More information: [https://developer.hashicorp.com/terraform/cli/commands/stacks/configuration](https://developer.hashicorp.com/terraform/cli/commands/stacks/configuration).

- List configurations for a Stack by organization, project, and Stack name:

`terraform stacks configuration list -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`

- Upload configuration for a Stack by organization, project, and Stack name:

`terraform stacks configuration upload -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`

- Fetch configuration for a Stack by organization, project, and Stack name:

`terraform stacks configuration fetch -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`

- Watch the latest configuration for a Stack by organization, project, and Stack name:

`terraform stacks configuration watch -organization-name {{organization}} -project-name {{project}} -stack-name {{stack_name}}`
