# podman ps

> List Podman containers.
> More information: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- List currently running Podman containers:

`podman ps`

- List all Podman containers (running and stopped):

`podman ps {{[-a|--all]}}`

- Show the latest created container (includes all states):

`podman ps {{[-l|--latest]}}`

- Filter containers that contain a substring in their name:

`podman ps {{[-f|--filter]}} "name={{name}}"`

- Filter containers that share a given image as an ancestor:

`podman ps {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Filter containers by exit status code:

`podman ps {{[-al|--all --filter]}} "exited={{code}}"`

- Filter containers by status (created, running, removing, paused, exited and dead):

`podman ps {{[-f|--filter]}} "status={{status}}"`

- Filter containers that mount a specific volume or have a volume mounted in a specific path:

`podman ps {{[-f|--filter]}} "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
