# kubectl rollout

> Verwalten des Rollouts einer Kubernetes-Ressource (deployments, daemonsets, and statefulsets).
> Mehr Informationen: <https://kubernetes.io/docs/reference/generated/kubectl/kubectl-commands#rollout>.

- Start eines rollenden Neustarts einer Ressource:

`kubectl rollout restart {{resource_type}}/{{resource_name}}`

- Überwachen Sie den fortlaufenden Aktualisierungsstatus einer Ressource:

`kubectl rollout status {{resource_type}}/{{resource_name}}`

- Zurücksetzen einer Ressource auf die vorherige Version:

`kubectl rollout undo {{resource_type}}/{{resource_name}}`

- Zeigt den Rollout-Verlauf einer Ressource:

`kubectl rollout history {{resource_type}}/{{resource_name}}`
