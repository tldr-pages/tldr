# docker stats

> Display a live stream of containers resource usage statistics.
> More information: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Display live stream of all running containers statistics:

`docker stats`

- Display live stream statistics of a space-separated list of containers:

`docker stats {{container_name}}`

- Change columns format to display containers cpu usage percentage:

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- Display all containers (running and stopped):

`docker stats --all`

- Disable streaming stats and only pull the current stats:

`docker stats --no-stream`
