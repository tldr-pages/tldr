# docker swarm

> Outil d'orchestration de conteneurs.
> Plus d'informations : <https://docs.docker.com/engine/swarm/>.

- Initialise un cluster swarm :

`docker swarm init`

- Affiche le jeton pour rejoindre un cluster swarm en tant que nœud manager ou worker :

`docker swarm join-token {{worker|manager}}`

- Rejoint un nouveau nœud au cluster :

`docker swarm join --token {{jeton}} {{url_du_manager:2377}}`

- Supprime un worker du cluster (à exécuter dans le nœud worker) :

`docker swarm leave`

- Affiche le certificat CA actuel au format PEM :

`docker swarm ca`

- Change le certificat CA actuel et affiche le nouveau certificat :

`docker swarm ca --rotate`

- Change la période de validité des certificats des nœuds :

`docker swarm update --cert-expiry {{heures}}h{{minutes}}m{{secondes}}s`
