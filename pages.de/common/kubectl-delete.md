# kubectl delete

> Lösche Kubernetes-Ressourcen.
> Weitere Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

- Löschen eines bestimmten Pods:

`kubectl delete pod {{pod_name}}`

- Lösche ein bestimmtes Deployment:

`kubectl delete deployment {{deployment_name}}`

- Lösche einer bestimmten Node:

`kubectl delete node {{node_name}}`

- Lösche alle Pods in einem bestimmten Namespaces:

`kubectl delete pods --all --namespace {{namespace}}`

- Lösche alle Deployments und Services in einem bestimmten Namespace:

`kubectl delete deployments,services --all --namespace {{namespace}}`

- Alle Nodes löschen:

`kubectl delete nodes --all`

- Lösche Resourcen, welche in einer YAML Datei definiert sind :

`kubectl delete --filename {{pfad/zu/manifest.yaml}}`
