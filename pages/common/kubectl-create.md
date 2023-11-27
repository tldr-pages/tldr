# kubectl create

> Create a resource from a file or from `stdin`.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#create>.

- Create a resource using the resource definition file:

`kubectl create -f {{path/to/file.yml}}`

- Create a resource from `stdin`:

`kubectl create -f -`

- Create a deployment:

`kubectl create deployment {{deployment_name}} --image={{image}}`

- Create a deployment with replicas:

`kubectl create deployment {{deployment_name}} --image={{image}} --replicas={{number_of_replicas}}`

- Create a service:

`kubectl create service {{service_type}} {{service_name}} --tcp={{port}}:{{target_port}}`

- Create a namespace:

`kubectl create namespace {{namespace_name}}`
