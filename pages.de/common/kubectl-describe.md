# kubectl describe

> Details von Kubernetes-Objekten und -Ressourcen anzeigen.
> Weitere Informationen: <https://kubernetes.io/docs/reference/kubectl/generated/kubectl_describe>.

- Zeige Details zu Pods in einem bestimmten [n]amespace an:

`kubectl describe {{[po|pods]}} {{[-n|--namespace]}} {{namespace}}`

- Zeige Details zu Nodes in einem bestimmten [n]amespace an:

`kubectl describe {{[no|nodes]}} {{[-n|--namespace]}} {{namespace}}`

- Zeige Details zu einem bestimmten Pod in einem bestimmten [n]amespace an:

`kubectl describe {{[po|pods]}} {{pod_name}} {{[-n|--namespace]}} {{namespace}}`

- Zeige Details zu einer bestimmten Node in einem bestimmten [n]amespace an:

`kubectl describe {{[no|nodes]}} {{node_name}} {{[-n|--namespace]}} {{namespace}}`

- Zeige Details zu Ressourcen, die in einer YAML Datei definiert sind, an:

`kubectl describe {{[-f|--filename]}} {{pfad/zu/manifest.yaml}}`
