# terraform destroy

> Destroy all objects managed by a Terraform configuration.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/destroy>.

- Destroy all infrastructure in the current directory:

`terraform destroy`

- Destroy infrastructure, skipping interactive approval:

`terraform destroy -auto-approve`

- Destroy a specific resource:

`terraform destroy -target {{resource_type.resource_name[instance_index]}}`

- Specify values for input variables:

`terraform destroy -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- Specify values for input variables from a file:

`terraform destroy -var-file {{path/to/file.tfvars}}`

- Destroy infrastructure with compact warnings:

`terraform destroy -compact-warnings`
