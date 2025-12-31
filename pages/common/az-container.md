# az container

> Manage Azure Container Instances.
> Part of `azure-cli` (also known as `az`).
> More information: <https://learn.microsoft.com/cli/azure/container>.

- Create a container in a container group:

`az container create {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{name}} --image {{image_name}} {{[-os|--os-type]}} {{windows|linux}} --cpu {{number_of_CPU_cores}} --memory {{memory_in_GB}}`

- Execute a command from within a running container of a container group:

`az container exec {{[-g|--resource-group]}} {{resource_group}} {{[-n|--name]}} {{container_group_name}} --exec-command "{{command}}"`

- Examine the logs of a container in a container group:

`az container logs {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Get the details of a container group:

`az container show {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Start all containers in a container group:

`az container start {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Stop all containers in a container group:

`az container stop {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`

- Delete a container group:

`az container delete {{[-n|--name]}} {{name}} {{[-g|--resource-group]}} {{resource_group}}`
