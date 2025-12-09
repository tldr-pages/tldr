# kubectl create

> Create a resource from a file or from `stdin`.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_create>.

- Create a resource using the resource definition file:

`kubectl create {{[-f|--filename]}} {{path/to/file.yml}}`

- Create a resource from `stdin`:

`kubectl create {{[-f|--filename]}} -`

- Create a deployment:

`kubectl create {{[deploy|deployment]}} {{deployment_name}} --image {{image}}`

- Create a deployment with replicas:

`kubectl create {{[deploy|deployment]}} {{deployment_name}} --image {{image}} --replicas {{number_of_replicas}}`

- Create a service:

`kubectl create {{[svc|service]}} {{service_type}} {{service_name}} --tcp {{port}}:{{target_port}}`

- Create a namespace:

`kubectl create {{[ns|namespace]}} {{namespace_name}}`
