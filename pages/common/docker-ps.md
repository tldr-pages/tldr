# docker ps

> List Docker containers.
> More information: <https://docs.docker.com/engine/reference/commandline/ps/>.

- List currently running Docker containers:

`docker ps`

- List all Docker containers (running and stopped):

`docker ps --all`

- Show the latest created container (includes all states):

`docker ps --latest`

- Filter containers that contain a substring in their name:

`docker ps --filter "name={{name}}"`

- Filter containers that share a given image as an ancestor:

`docker ps --filter "ancestor={{image}}:{{tag}}"`

- Filter containers by exit status code:

`docker ps --all --filter="exited={{code}}"`

- Filter containers by status (created, running, removing, paused, exited and dead):

`docker ps --filter "status={{status}}"`

- Filter containers that mount a specific volume or have a volume mounted in a specific path:

`docker ps --filter "volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
