# kubectl edit

> Edit Kubernetes resources.
> More information: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_edit>.

- Edit a pod in the default namespace:

`kubectl edit {{[po|pods]}}/{{pod_name}}`

- Edit a deployment in the default namespace:

`kubectl edit {{[deploy|deployment]}}/{{deployment_name}}`

- Edit a service in the default namespace:

`kubectl edit {{[svc|service]}}/{{service_name}}`

- Edit all entries of a given resource in a given namespace:

`kubectl edit {{resource}} {{[-n|--namespace]}} {{namespace}}`

- Edit a resource using a specific editor:

`KUBE_EDITOR={{nano}} kubectl edit {{resource}}/{{resource_name}}`

- Edit a resource in JSON format:

`kubectl edit {{resource}}/{{resource_name}} {{[-o|--output]}} json`
