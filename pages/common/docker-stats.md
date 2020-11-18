# docker stats

> Display a live stream of resource usage statistics for containers.
> More information: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Display a live stream for the statistics of all running containers:

`docker stats`

- Display a live stream of statistics for a space-separated list of containers:

`docker stats {{container_name}}`

- Change the columns format to display container's cpu usage percentage:

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- Display statistics for all containers (both running and stopped):

`docker stats --all`

- Disable streaming stats and only pull the current stats:

`docker stats --no-stream`
