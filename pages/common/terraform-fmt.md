# terraform fmt

> Format configuration according to Terraform language style conventions.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/fmt>.

- Format the configuration in the current directory:

`terraform fmt`

- Format the configuration in the current directory and subdirectories:

`terraform fmt -recursive`

- Display diffs of formatting changes:

`terraform fmt -diff`

- Do not list files that were formatted to `stdout`:

`terraform fmt -list=false`
