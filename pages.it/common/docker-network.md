# docker network

> Crea e gestisci reti docker.
> Maggiori informazioni: <https://docs.docker.com/engine/reference/commandline/network/>.

- Elenca le reti disponibili configurate sul Docker daemon:

`docker network ls`

- Crea una rete definita da un utente:

`docker network create --driver {{nome_del_driver}} {{nome_rete}}`

- Mostra informazioni dettagliate su una lista di reti (separata da spazi):

`docker network inspect {{nome_rete_1 nome_rete_2}}`

- Connetti un container ad una rete usando il suo nome o ID:

`docker network connect {{nome_rete}} {{nome_container|ID}}`

- Disconnetti un container da una rete:

`docker network disconnect {{nome_rete}} {{nome_container|ID}}`

- Elimina le reti inutilizzate (non referenziate da alcun container):

`docker network prune`

- Elimina una lista di reti (separata da spazi) inutilizzate:

`docker network rm {{nome_rete_1 nome_rete_2}}`
