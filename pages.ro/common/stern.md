# stern

> Coada mai multe păstăi și containere de la Kubernetes.
> Mai multe informaţii: <https://github.com/wercker/stern/>

- Coada toate păstăile într-un spațiu de nume curent:

`stern .`

- Coada toate păstăile cu un statut specific:

`stern . --container-state {{running|waiting|terminated}}`

- Coada toate păstăi care se potrivește cu o expresie regulată dată:

`stern {{pod_query}}`

- Coada de păstăi potrivite din toate spațiile de nume:

`stern {{pod_query}} --all-namespaces`

- Coada de păstăi potrivite de 15 minute în urmă:

`stern {{pod_query}} --since {{15m}}`

- Coada păstăi potrivite cu o etichetă specifică:

`stern {{pod_query}} --selector {{release=canary}}`
