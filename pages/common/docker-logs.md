# docker logs

> Print container logs.
> More information: <https://docs.docker.com/engine/reference/commandline/logs>.

- Print logs from a container:

`docker logs {{container_name}}`

- Print logs and follow them:

`docker logs -f {{container_name}}`

- Print last 5 lines:

`docker logs {{container_name}} --tail {{5}}`

- Print logs and append them with timestamps:

`docker logs -t {{container_name}}`

- Print logs from a certain point in time of container execution (i.e. 23m, 10s, 2013-01-02T13:23:37):

`docker logs {{container_name}} --until {{time}}`
