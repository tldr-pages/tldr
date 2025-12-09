# k8s-unused-secret-detector

> Detect unused Kubernetes secrets.
> More information: <https://github.com/dtan4/k8s-unused-secret-detector>.

- Detect unused secrets:

`k8s-unused-secret-detector`

- Detect unused secrets in a specific namespace:

`k8s-unused-secret-detector {{[-n|--namespace]}} {{namespace}}`

- Delete unused secrets in a specific namespace:

`k8s-unused-secret-detector {{[-n|--namespace]}} {{namespace}} | kubectl delete secrets {{[-n|--namespace]}} {{namespace}}`
