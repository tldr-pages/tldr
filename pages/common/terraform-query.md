# terraform query

> Query remote infrastructure for resources matching criteria in `.tfquery.hcl` files.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/query>.

- Query infrastructure using `.tfquery.hcl` files in the current directory:

`terraform query`

- Query and generate import blocks and resource configuration:

`terraform query -generate-config-out {{path/to/generated.tf}}`

- Specify values for input variables defined in the query file:

`terraform query -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Specify values for input variables from a file:

`terraform query -var-file {{path/to/file.tfvars}}`

- Output results in JSON format:

`terraform query -json`
