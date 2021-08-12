# docker swarm

> Un instrument de orchestrare a containerelor.
> Mai multe informaţii: <https://docs.docker.com/engine/swarm/>

- Iniţializează un grup de roi:

`docker swarm init`

- Afișează token-ul pentru a se alătura unui manager sau unui lucrător:

`docker swarm join-token {{worker|manager}}`

- Alăturați-vă unui nou nod la cluster:

`docker swarm join --token {{token}} {{manager_node_url:2377}}`

- Scoateți un lucrător din roi (rulați în interiorul nodului lucrător):

`docker swarm leave`

- Afișează certificatul CA curent în format PEM:

`docker swarm ca`

- Rotiți certificatul CA curent și afișați noul certificat:

`docker swarm ca --rotate`

- Modificați perioada validă pentru certificatele de nod:

`docker swarm update --cert-expiry {{hours}}h{{minutes}}m{{seconds}}s`
