# terraform taint

> Mark a resource instance as not fully functional to force replacement on next apply.
> Note: This command is deprecated. Use `terraform apply -replace` instead.
> See also: `terraform apply`, `terraform untaint`.
> More information: <https://developer.hashicorp.com/terraform/cli/commands/taint>.

- Mark a resource as tainted:

`terraform taint {{resource_type.resource_name[instance_index]}}`

- Mark a resource as tainted, even if the resource is missing:

`terraform taint -allow-missing {{resource_type.resource_name[instance_index]}}`

- Mark a resource as tainted without acquiring a state lock:

`terraform taint -lock=false {{resource_type.resource_name[instance_index]}}`

- Mark a resource as tainted with a custom lock timeout:

`terraform taint -lock-timeout={{duration}} {{resource_type.resource_name[instance_index]}}`
