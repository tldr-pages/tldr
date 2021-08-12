# popeye

> Utilitate care raportează probleme potențiale cu Kubernetes implementare se manifestă.
> Mai multe informaţii: <https://github.com/derailed/popeye>

- Scanează clusterul Kubernetes curent:

`popeye`

- Scanați un anumit spațiu de nume:

`popeye -n {{namespace}}`

- Scanare context specific Kubernetes:

`popeye --context={{context}}`

- Utilizați un fișier de configurare spanac pentru scanare:

`popeye -f {{spinach.yaml}}`
