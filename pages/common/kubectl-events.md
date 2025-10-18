# kubectl events

> List and watch events in the cluster.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_events/>.

- List recent events in the default namespace:

`kubectl events`

- List events for all namespaces:

`kubectl events --all-namespaces`

- List events for a specific namespace:

`kubectl events --namespace {{namespace_name}}`

- List events for a specific object:

`kubectl events --for {{pod}}/{{pod_name}}`

- Watch for new events in real-time:

`kubectl events --watch`

- List events and filter by type (Normal or Warning):

`kubectl events --types {{Warning}}`
