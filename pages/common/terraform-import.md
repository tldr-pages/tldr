# terraform import

> Import existing infrastructure into Terraform state.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/import>.

- Import an existing resource into Terraform state:

`terraform import {{resource_type.resource_name}} {{resource_id}}`

- Import a resource into a module:

`terraform import module.{{module_name}}.{{resource_type.resource_name}} {{resource_id}}`

- Import without interactive input prompts (useful for automation):

`terraform import -input=false {{resource_type.resource_name}} {{resource_id}}`

- Import with variable values:

`terraform import -var '{{name}}={{value}}' {{resource_type.resource_name}} {{resource_id}}`

- Import with a variable file:

`terraform import -var-file={{path/to/variables.tfvars}} {{resource_type.resource_name}} {{resource_id}}`

- Import without state locking (use with caution):

`terraform import -lock=false {{resource_type.resource_name}} {{resource_id}}`
