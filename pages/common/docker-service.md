# docker service

> Manage services in swarm mode.
> More information: <https://docs.docker.com/engine/reference/commandline/service/>.

- List services:

`docker service ls`

- List the tasks of services:

`docker service ps`

- Create new service:

`docker service create --name {{service_name}} {{image}}`

- Create new service with 5 replica:

`docker service create --name {{container_name}} --replicas={{5}} {{image}}`

- Delete service:

`docker service {{service_name}}`

- Scale multiple replicated services:

`docker service {{service_name_1=replica_count}} {{service_name_2=replica_count}}`

- Exposing port of a published service:

`docker service update --publish-add published=8080,target=80 {{service_name}}`

- Rollback the service to its previous version:

`docker service rollback {{service_name}}`
