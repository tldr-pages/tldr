# docker inspect

> Return low-level information on Docker objects.
> More information: <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Show help:

`docker inspect`

- Display information for a container, image or volume using name or ID:

`docker inspect {{container|image|ID}}`

- Display a container IP address:

`docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {{container}}`

- Display the path to the container's log file:

`docker inspect --format='{{.LogPath}}' {{container}}`

- Display the image name of the container:

`docker inspect --format='{{.Config.Image}}' {{container}}`

- Display configuration information in JSON format:

`docker inspect --format='{{json .Config}}' {{container}}`

- Display all port bindings:

`docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' {{container}}`
