# docker swarm

> A container orchestration tool.
> More information: <https://docs.docker.com/engine/swarm/>.

- Initialize a swarm cluster:

`docker swarm init`

- Get join token for master or worker:

`docker swarm join-token {{type}}`

- Join new node to cluster:

`docker swarm join --token {{token}} {{manager_node_url:2377}}`

- Leave the cluster:

`docker swarm leave`

- View current CA certificate:

`docker swarm ca`

- Rotate current CA certificate:

`docker swarm ca --rotate`

- Change cert expiration time with (ns,us,ms,sm,h) time unit:

`docker swarm update --cert-expiry {{2160h0m0s}}`
