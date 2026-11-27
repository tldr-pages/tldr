# podman logs

> Display the logs of one or more containers.
> More information: <https://docs.podman.io/en/latest/markdown/podman-logs.1.html>.

- Display the logs of a container:

`podman logs {{container_name}}`

- Display the logs of a container and follow log output:

`podman logs {{[-f|--follow]}} {{container_name}}`

- Display the last 10 lines of logs:

`podman logs --tail 10 {{container_name}}`

- Display the logs with timestamps:

`podman logs {{[-t|--timestamps]}} {{container_name}}`

- Display the logs generated in the last 10 minutes:

`podman logs --since 10m {{container_name}}`

- Display the logs of multiple containers, prefixed with the container name:

`podman logs {{[-n|--names]}} {{container_name1 container_name2 ...}}`

- Display the logs of the latest created container:

`podman logs {{[-l|--latest]}}`
