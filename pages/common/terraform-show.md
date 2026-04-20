# terraform show

> Read and output a Terraform state or plan file in human-readable form.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/show>.

- Show the current state:

`terraform show`

- Show a specific state file:

`terraform show {{path/to/terraform.tfstate}}`

- Show a specific plan file:

`terraform show {{path/to/file.tfplan}}`

- Output in JSON format:

`terraform show -json`

- Output a plan file in JSON format:

`terraform show -json {{path/to/file.tfplan}}`

- Write to a file without color codes:

`terraform show -no-color > {{path/to/file}}`
