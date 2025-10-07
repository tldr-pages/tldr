# kubectl scale

> Set a new size for a deployment, replica set, replication controller, or stateful set.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_scale>.

- Scale a replica set:

`kubectl scale --replicas {{replicas_count}} rs/{{replica_name}}`

- Scale a resource identified by a file:

`kubectl scale --replicas {{replicas_count}} {{[-f|--filename]}} {{path/to/file.yml}}`

- Scale a deployment based on current number of replicas:

`kubectl scale --replicas {{replicas_count}} --current-replicas {{current_replicas}} {{[deploy|deployment]}}/{{deployment_name}}`
