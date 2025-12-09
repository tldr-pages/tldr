# kubectl auth

> Inspect access permissions in a Kubernetes cluster.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_auth>.

- Check if the current user can perform all actions on all resources in a specific namespace:

`kubectl auth can-i '*' '*' {{[-n|--namespace]}} {{namespace}}`

- Check if the current user can perform a specific verb on a specific resource:

`kubectl auth can-i {{verb}} {{resource}} {{[-n|--namespace]}} {{namespace}}`

- Check if a specific user or service account can perform an action on a resource:

`kubectl auth can-i {{verb}} {{resource}} {{[-n|--namespace]}} {{namespace}} --as {{user_or_sa}}`

- List all actions the current user is allowed to perform in a namespace:

`kubectl auth can-i --list {{[-n|--namespace]}} {{namespace}}`
