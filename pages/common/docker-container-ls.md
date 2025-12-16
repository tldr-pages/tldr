# docker container ls

> List Docker containers.
> More information: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- List currently running Docker containers:

`docker {{[ps|container ls]}}`

- List all Docker containers (running and stopped):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Show the latest created container (includes all states):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Filter containers that contain a substring in their name:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{name}}"`

- Filter containers that share a given image as an ancestor:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Filter containers by exit status code:

`docker {{[ps|container ls]}} {{[-a|--all]}} {{[-f|--filter]}} "exited={{code}}"`

- Filter containers by status (created, running, removing, paused, exited and dead):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{status}}"`

- Filter containers that mount a specific volume or have a volume mounted in a specific path:

`docker ps {{[-f|--filter]}} "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
