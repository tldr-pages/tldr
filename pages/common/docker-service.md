# docker service

> Manage the services on a docker daemon.
> More information: <https://docs.docker.com/engine/reference/commandline/service/>.

- List the services on a docker daemon:

`docker service ls`

- Create a new service:

`docker service create --name {{service_name}} {{image}}:{{tag}}`

- Display detailed information of a space-separated list of services:

`docker service inspect {{service_name|ID}}`

- List the tasks of a space-separated list of services:

`docker service ps {{service_name|ID}}`

- Scale to a specific number of replicas for a space-separated list of services:

`docker service scale {{service_name}}={{count_of_replicas}}`

- Remove a space-separated list of services:

`docker service rm {{service_name|ID}}`
