# kubectl events

> Display resource events.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_events/>.

- Show events in the default namespace:

`kubectl events`

- Show events in all namespaces:

`kubectl events {{[-A|--all-namespaces]}}`

- Watch events in a specific namespace:

`kubectl events {{[-w|--watch]}} {{[-n|--namespace]}} {{namespace}}`

- Show events for a pod in a specific namespace:

`kubectl events --for {{pod}}/{{pod_name}} {{[-n|--namespace]}} {{namespace}}`

- Show events for a resource in a specific namespace:

`kubectl events --for {{resource}}/{{resource_name}} {{[-n|--namespace]}} {{namespace}}`

- Show events for type `Warning` or `Normal`:

`kubectl events --types=Warning,Normal`

- Output events in YAML format:

`kubectl events {{[-o|--output]}} yaml`
