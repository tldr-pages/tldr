# docker system

> Manage Docker data and display system-wide information.
> More information: <https://docs.docker.com/reference/cli/docker/system/>.

- Show Docker disk usage:

`docker system df`

- Show detailed information on disk usage:

`docker system df {{[-v|--verbose]}}`

- Remove unused data (append `--volumes` to remove unused volumes as well):

`docker system prune`

- Remove unused data created more than a specified amount of time in the past:

`docker system prune --filter "until={{hours}}h{{minutes}}m"`

- Display real-time events from the Docker daemon:

`docker system events`

- Display real-time events from containers streamed as valid JSON Lines:

`docker system events {{[-f|--filter]}} 'type=container' --format '{{json .}}'`

- Display system-wide information:

`docker system info`

- Display help:

`docker system`
