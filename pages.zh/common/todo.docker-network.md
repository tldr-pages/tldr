# docker network

> Create and manage docker networks.
> More information: <https://docs.docker.com/engine/reference/commandline/network/>.

- List all available and configured networks on docker daemon:

`docker network ls`

- Create a user defined network:

`docker network create --driver {{driver_name}} {{network_name}}`

- Display detailed information of a space-separated list of networks:

`docker network inspect {{network_name}}`

- Connect a container to a network using a name or ID:

`docker network connect {{network_name}} {{container_name|ID}}`

- Disconnect a container from a network:

`docker network disconnect {{network_name}} {{container_name|ID}}`

- Remove all unused (not referenced by any container) networks:

`docker network prune`

- Remove a space-separated list of unused networks:

`docker network rm {{network_name}}`
