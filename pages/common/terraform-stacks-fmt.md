# terraform stacks fmt

> Rewrite deployment and component configuration files for a Stack to a canonical format.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/stacks/fmt>.

- Format all configuration files in the current directory:

`terraform stacks fmt`

- Format a specific file:

`terraform stacks fmt {{path/to/file.tfstack.hcl}}`

- Show formatting differences without making changes:

`terraform stacks fmt -diff`

- Format files recursively in subdirectories:

`terraform stacks fmt -recursive`
