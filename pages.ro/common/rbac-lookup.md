# rbac-lookup

> Găsiți roluri și roluri de cluster atașate oricărui utilizator, cont de serviciu sau nume de grup din clusterul Kubernetes.
> Mai multe informaţii: <https://github.com/reactiveops/rbac-lookup>

- Vezi toate legăturile RBAC:

`rbac-lookup`

- Vezi legăturile RBAC care se potrivesc cu o anumită expresie:

`rbac-lookup {{search_term}}`

- Vizualizaţi toate legăturile RBAC împreună cu legarea rolului sursă:

`rbac-lookup -o wide`

- Vezi toate legăturile RBAC filtrate după subiect:

`rbac-lookup -k {{user|group|serviceaccount}}`

- Vizualizați toate legăturile RBAC împreună cu rolurile IAM (dacă utilizați GKE):

`rbac-lookup --gke`
