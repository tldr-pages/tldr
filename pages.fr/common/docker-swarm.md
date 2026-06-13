# docker swarm

> Outil d'orchestration de conteneurs.
> Plus d'informations : <https://docs.docker.com/engine/swarm/>.

- Initialiser un cluster swarm :

`docker swarm init`

- Afficher le jeton pour rejoindre un cluster swarm en tant que nœud manager ou worker :

`docker swarm join-token {{worker|manager}}`

- Rejoindre un nouveau nœud au cluster :

`docker swarm join --token {{jeton}} {{url_du_manager:2377}}`

- Supprimer un worker du cluster (à exécuter dans le nœud worker) :

`docker swarm leave`

- Afficher le certificat CA actuel au format PEM :

`docker swarm ca`

- Changer la certificat CA actuel et afficher le nouveau certificat :

`docker swarm ca --rotate`

- Changer la période de validité des certificats des nœuds :

`docker swarm update --cert-expiry {{heures}}h{{minutes}}m{{secondes}}s`
