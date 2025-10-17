# kubectl-explain

> Display the documentation of a Kubernetes API resource, including available fields and descriptions.
> More information: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands/#explain>.

- Show documentation for a resource:

`kubectl explain {{pods|nodes|deployments|...}}`

- Show documentation for a sub-resource or field of an object:

`kubectl explain {{pod.spec.containers}}`

- Show documentation for a specific versioned resource:

`kubectl explain {{ingress.v1.networking.k8s.io}}`

- Show all fields recursively for a resource:

`kubectl explain {{pod}} --recursive`

- Display help:

`kubectl explain --help`
