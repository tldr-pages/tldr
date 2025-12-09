# docker inspect

> Erhalte tiefgehende Informationen zu Docker Objekten.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/inspect/>.

- Zeige Hilfeseite:

`docker inspect`

- Zeige Informationen über einen Container, ein Image oder Volume anhand des Namens oder der ID:

`docker inspect {{container|image|ID}}`

- Zeige die IP Adresse eines Containers an:

`docker inspect {{[-f|--format]}} '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{container}}`

- Zeige den Pfad zur Logdatei eines Containers:

`docker inspect {{[-f|--format]}} '\{\{.LogPath\}\}' {{container}}`

- Zeige den Namen des Images eines Containers:

`docker inspect {{[-f|--format]}} '\{\{.Config.Image\}\}' {{container}}`

- Zeige die Konfiguration als JSON an:

`docker inspect {{[-f|--format]}} '\{\{json .Config\}\}' {{container}}`

- Zeige alle Port Bindings:

`docker inspect {{[-f|--format]}} '\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{container}}`
