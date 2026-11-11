# terraform state

> Perform advanced state management in Terraform.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/state>.

- List all resources in the state:

`terraform state list`

- Show the attributes of a single resource in the state:

`terraform state show {{resource_type.resource_name}}`

- Move a resource to a new address:

`terraform state mv {{source_resource}} {{destination_resource}}`

- Remove a resource from the state without destroying the real infrastructure:

`terraform state rm {{resource_type.resource_name}}`

- Download and output the current remote state to `stdout`:

`terraform state pull`

- Upload a local state file to the remote backend:

`terraform state push {{path/to/state.json}}`
