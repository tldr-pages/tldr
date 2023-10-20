# kubectl edit

> Expose a resource as a new Kubernetes service.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#expose>.

- Create a service for a resource, which will be served from container port to node port:

`kubectl expose {{resource_type}} {{resource_name}} --port={{node_port}} --target-port={{container_port}}`

- Create a service for a resource identified by a file:

`kubectl expose -f {{path/to/file.yml}} --port={{node_port}} --target-port={{container_port}}`

- Create a service with a name, to serve to a node port which will be same for container port:

`kubectl expose {{resource_type}} {{resource_name}} --port={{node_port}} --name={{service_name}}`
