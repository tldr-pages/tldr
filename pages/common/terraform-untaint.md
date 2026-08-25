# terraform untaint

> Remove the tainted status from a resource instance.
> See also: `terraform taint`.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/untaint>.

- Remove tainted status from a resource:

`terraform untaint {{resource_type.resource_name[instance_index]}}`

- Remove tainted status, even if the resource is missing:

`terraform untaint -allow-missing {{resource_type.resource_name[instance_index]}}`

- Remove tainted status without acquiring a state lock:

`terraform untaint -lock=false {{resource_type.resource_name[instance_index]}}`

- Remove tainted status with a custom lock timeout:

`terraform untaint -lock-timeout={{duration}} {{resource_type.resource_name[instance_index]}}`
