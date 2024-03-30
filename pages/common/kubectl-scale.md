# kubectl scale

> Set a new size for a deployment, replica set, replication controller, or stateful set.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#scale>.

- Scale a replica set:

`kubectl scale --replicas={{number_of_replicas}} rs/{{replica_name}}`

- Scale a resource identified by a file:

`kubectl scale --replicas={{number_of_replicas}} -f {{path/to/file.yml}}`

- Scale a deployment based on current number of replicas:

`kubectl scale --current-replicas={{current_replicas}} --replicas={{number_of_replicas}} deployment/{{deployment_name}}`
