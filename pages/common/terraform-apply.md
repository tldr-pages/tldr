# terraform apply

> Create or update infrastructure according to Terraform configuration files.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/apply>.

- Create or update infrastructure:

`terraform apply`

- Create or update infrastructure, skipping interactive approval:

`terraform apply -auto-approve`

- Apply a plan file:

`terraform apply {{path/to/file.tfplan}}`

- Specify values for input variables:

`terraform apply -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Specify values for input variables from a file:

`terraform apply -var-file {{path/to/file.tfvars}}`

- Apply changes to a specific resource:

`terraform apply -target {{resource_type.resource_name[instance_index]}}`

- Replace a specific resource:

`terraform apply -replace {{resource_type.resource_name[instance_index]}}`

- Destroy Terraform-managed infrastructure:

`terraform apply -destroy`
