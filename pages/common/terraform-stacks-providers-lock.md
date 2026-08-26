# terraform stacks providers-lock

> Create or update the dependency lock file for the current component configuration.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/stacks/providers-lock>.

- Create or update the lock file for the current platform:

`terraform stacks providers-lock`

- Create or update the lock file with checksums for multiple platforms:

`terraform stacks providers-lock -platform={{linux_amd64}} -platform={{darwin_amd64}}`
