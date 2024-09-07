# docker service

> Manage the services on a Docker daemon.
> More information: <https://docs.docker.com/engine/reference/commandline/service/>.

- List the services on a Docker daemon:

`docker service ls`

- Create a new service:

`docker service create --name {{service_name}} {{image}}:{{tag}}`

- Display detailed information about one or more services:

`docker service inspect {{service_name_or_ID1 service_name_or_ID2}}`

- List the tasks of one or more services:

`docker service ps {{service_name_or_ID1 service_name_or_ID2 ...}}`

- Scale to a specific number of replicas for a space-separated list of services:

`docker service scale {{service_name}}={{count_of_replicas}}`

- Remove one or more services:

`docker service rm {{service_name_or_ID1 service_name_or_ID2}}`
