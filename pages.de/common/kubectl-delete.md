# kubectl delete

> Löschen von Kubernetes-Ressourcen.
> Mehr Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#delete>.

- Löschen eines bestimmten Pods:

`kubectl delete pod {{pod_name}}`

- Löschen eines bestimmten Deployments:

`kubectl delete deployment {{deployment_name}}`

- Löschen eines bestimmten Nodes:

`kubectl delete node {{node_name}}`

- Löschen aller Pods in einem bestimmten Namespaces:

`kubectl delete pods --all --namespace {{namespace}}`

- Löschen aller Deployments und Services in einem bestimmten Namespace:

`kubectl delete deployments,services --all --namespace {{namespace}}`

- Alle Nodes löschen:

`kubectl delete nodes --all`

- Löschen von Resourcen, welche in einer YAML Datei definiert sind :

`kubectl delete --filename {{pfad/zu/manifest}}.yaml`
