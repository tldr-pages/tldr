# docker inspect

> Return low-level information on Docker objects.
> More information: <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Display help:

`docker inspect`

- Display information about a container, image, or volume using a name or ID:

`docker inspect {{container|image|ID}}`

- Display a container's IP address:

`docker inspect --format '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{container}}`

- Display the path to the container's log file:

`docker inspect --format='\{\{.LogPath\}\}' {{container}}`

- Display the image name of the container:

`docker inspect --format='\{\{.Config.Image\}\}' {{container}}`

- Display the configuration information as JSON:

`docker inspect --format='\{\{json .Config\}\}' {{container}}`

- Display all port bindings:

`docker inspect --format='\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{container}}`
