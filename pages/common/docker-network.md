# docker network

> Create and manage Docker networks.
> More information: <https://docs.docker.com/reference/cli/docker/network/>.

- List all available and configured networks on Docker daemon:

`docker network ls`

- Create a user-defined network:

`docker network create {{[-d|--driver]}} {{driver_name}} {{network_name}}`

- Display detailed information about one or more networks:

`docker network inspect {{network_name1 network_name2 ...}}`

- Connect a container to a network using a name or ID:

`docker network connect {{network_name}} {{container_name|ID}}`

- Disconnect a container from a network:

`docker network disconnect {{network_name}} {{container_name|ID}}`

- Remove all unused (not referenced by any container) networks:

`docker network prune`

- Remove one or more unused networks:

`docker network rm {{network_name1 network_name2 ...}}`
