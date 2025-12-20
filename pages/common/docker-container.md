# docker container

> Manage Docker containers.
> More information: <https://docs.docker.com/reference/cli/docker/container/>.

- List currently running Docker containers:

`docker {{[ps|container ls]}}`

- Start one or more stopped containers:

`docker {{[start|container start]}} {{container1_name}} {{container2_name}}`

- Kill one or more running containers:

`docker {{[kill|container kill]}} {{container_name}}`

- Stop one or more running containers:

`docker {{[stop|container stop]}} {{container_name}}`

- Pause all processes within one or more containers:

`docker {{[pause|container pause]}} {{container_name}}`

- Display detailed information on one or more containers:

`docker container inspect {{container_name}}`

- Export a container's filesystem as a tar archive:

`docker {{[export|container export]}} {{container_name}}`

- Create a new image from a container's changes:

`docker {{[commit|container commit]}} {{container_name}}`
