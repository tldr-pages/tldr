# kubectl describe

> Details von Kubernetes-Objekten und -Ressourcen anzeigen.
> Mehr Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#describe>.

- Details zu Pods in einem Namespace anzeigen:

`kubectl describe pods -n {{namespace}}`

- Details zu Nodes in einem Namespace anzeigen:

`kubectl describe nodes -n {{namespace}}`

- Details zu einem bestimmten Pod in einem Namespace anzeigen:

`kubectl describe pods {{pod_name}} -n {{namespace}}`

- Details zu einer bestimmten Node in einem Namespace anzeigen:

`kubectl describe nodes {{node_name}} -n {{namespace}}`

- Details zu Objekten anzeigen, welche in einer YAML Datei definiert sind:

`kubectl describe -f {{path/to/manifest}}.yaml`
