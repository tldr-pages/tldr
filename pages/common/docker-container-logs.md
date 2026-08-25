# docker container logs

> Print container logs.
> More information: <https://docs.docker.com/reference/cli/docker/container/logs/>.

- Print logs from a container:

`docker {{[logs|container logs]}} {{name|id}}`

- Print logs and follow them:

`docker {{[logs|container logs]}} {{name|id}} {{[-f|--follow]}}`

- Print last 5 lines:

`docker {{[logs|container logs]}} {{name|id}} {{[-n|--tail]}} 5`

- Print logs and append them with timestamps:

`docker {{[logs|container logs]}} {{name|id}} {{[-t|--timestamps]}}`

- Print logs from a certain point in time of container execution (i.e. 23m, 10s, 2013-01-02T13:23:37):

`docker {{[logs|container logs]}} {{name|id}} --until {{time}}`
