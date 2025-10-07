# kubectl api-resources

> Print the supported API resources on the server.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_api-resources>.

- Print the supported API resources:

`kubectl api-resources`

- Print the supported API resources with more information:

`kubectl api-resources {{[-o|--output]}} wide`

- Print the supported API resources sorted by a column:

`kubectl api-resources --sort-by {{name}}`

- Print the supported namespaced resources:

`kubectl api-resources --namespaced`

- Print the supported non-namespaced resources:

`kubectl api-resources --namespaced=false`

- Print the supported API resources with a specific API group:

`kubectl api-resources --api-group {{api_group}}`
