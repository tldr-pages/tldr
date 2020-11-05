# docker stats

> Display a live stream of containers resource usage statistics.
> More information: <https://docs.docker.com/engine/reference/commandline/stats/>.

- Display live stream of all running containers statistics:

`docker stats`

- Display live stream statistics on multiple containers by name or id:

`docker stats {{container_name container_id ...}}`

- Change columns format to display containers cpu usage percentage:

`docker stats --format "{{.Name}}:\t{{.CPUPerc}}"`

- Show all containers including non running containers:

`docker stats --all`

- Disable streaming stats and only pull the current stats:

`docker stats --no-stream`
