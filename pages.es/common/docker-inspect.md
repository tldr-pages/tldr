# docker inspect

> Muestra información de bajo nivel sobre objetos de Docker.
> Más información: <https://docs.docker.com/reference/cli/docker/inspect/>.

- Muestra información sobre un contenedor, imagen o volumen usando un nombre o ID:

`docker inspect {{contenedor|imagen|ID}}`

- Muestra la dirección IP de un contenedor:

`docker inspect {{[-f|--format]}} '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{contenedor}}`

- Muestra la ruta al archivo de log del contenedor:

`docker inspect {{[-f|--format]}} '\{\{.LogPath\}\}' {{contenedor}}`

- Muestra el nombre de la imagen del contenedor:

`docker inspect {{[-f|--format]}} '\{\{.Config.Image\}\}' {{contenedor}}`

- Muestra la información de configuración en formato JSON:

`docker inspect {{[-f|--format]}} '\{\{json .Config\}\}' {{contenedor}}`

- Muestra todos los enlaces de puertos:

`docker inspect {{[-f|--format]}} '\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{contenedor}}`

- Muestra la ayuda:

`docker inspect`
