# docker service

> Manage services.
> More information: <https://docs.docker.com/engine/reference/commandline/service/>.

- List services on docker daemon:

`docker service ls`

- Create a new service:

`docker service create --name --name {{service_name}} {{docker_image_name}}:{{image_version}}`

- Display detailed information on one or more space separated services:

`docker service inspect {{service_name|ID}}`

- List the tasks of one or more space separated services:

`docker service ps {{service_name|ID}}`

- Scale one or more space separated replicated services:

`docker service scale {{service_name}}={{no_of_replicas}}`

- Remove one or more space separated services:

`docker service rm {{service_name|ID}}`
