# kubectl delete

> Lösche Kubernetes-Ressourcen.
> Weitere Informationen: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_delete>.

- Lösche einen bestimmten Pod:

`kubectl delete {{[po|pod]}} {{pod_name}}`

- Lösche ein bestimmtes Deployment:

`kubectl delete {{[deploy|deployment]}} {{deployment_name}}`

- Lösche eine bestimmte Node:

`kubectl delete {{[no|node]}} {{node_name}}`

- Lösche alle Pods in einem bestimmten Namespaces:

`kubectl delete {{[po|pods]}} --all {{[-n|--namespace]}} {{namespace}}`

- Lösche alle Deployments und Services in einem bestimmten Namespace:

`kubectl delete {{[deploy|deployment]}},{{[svc|services]}} --all {{[-n|--namespace]}} {{namespace}}`

- Lösche alle Nodes:

`kubectl delete {{[no|nodes]}} --all`

- Lösche Resourcen, die in einer YAML Datei definiert sind:

`kubectl delete {{[-f|--filename]}} {{pfad/zu/manifest.yaml}}`
