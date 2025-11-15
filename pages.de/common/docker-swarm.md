# docker swarm

> Ein Container-Orchestrierungswerkzeug.
> Weitere Informationen: <https://docs.docker.com/engine/swarm/>.

- Initialisiere ein Swarm Cluster:

`docker swarm init`

- Zeige den Token um als Manager oder Worker beizutreten:

`docker swarm join-token {{worker|manager}}`

- Füge dem Cluster eine neue Node hinzu:

`docker swarm join --token {{token}} {{manager_node_url:2377}}`

- Entferne einen Worker vom Swarm (führe dies auf der Worker Node aus):

`docker swarm leave`

- Zeige die aktuellen CA Zertifikate im PEM Format:

`docker swarm ca`

- Rotiere die aktuellen CA Zertifikate und zeige die neuen Zertifikate:

`docker swarm ca --rotate`

- Ändere die Gültigkeitsdauer für Node-Zertifikate:

`docker swarm update --cert-expiry {{stunden}}h{{minuten}}m{{sekunden}}s`
