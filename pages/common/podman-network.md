# podman network

> Create and manage Podman networks.
> More information: <https://docs.podman.io/en/latest/markdown/podman-network.1.html>.

- List all available networks:

`podman network ls`

- Create a user-defined network:

`podman network create {{network_name}}`

- Display detailed information about one or more networks:

`podman network inspect {{network_name}}`

- Connect a container to a network:

`podman network connect {{network_name}} {{container_name}}`

- Disconnect a container from a network:

`podman network disconnect {{network_name}} {{container_name}}`

- Remove all unused networks:

`podman network prune`

- Remove one or more networks:

`podman network rm {{network_name}}`

- Check if a network exists:

`podman network exists {{network_name}}`
