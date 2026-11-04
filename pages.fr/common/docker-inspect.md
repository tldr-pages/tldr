# docker inspect

> Retour d'informations de bas niveau sur les objets Docker.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/inspect/>.

- Affiche les informations de configuration d'un conteneur, image ou volume en utilisant un nom ou un ID :

`docker inspect {{conteneur|image|id}}`

- Affiche l'adresse IP d'un conteneur :

`docker inspect {{[-f|--format]}} '\{\{range.NetworkSettings.Networks\}\}\{\{.IPAddress\}\}\{\{end\}\}' {{conteneur}}`

- Affiche le chemin du fichier journal d'un conteneur :

`docker inspect {{[-f|--format]}} '\{\{.LogPath\}\}' {{conteneur}}`

- Affiche le nom de l'image d'un conteneur :

`docker inspect {{[-f|--format]}} '\{\{.Config.Image\}\}' {{conteneur}}`

- Affiche les informations de configuration en JSON :

`docker inspect {{[-f|--format]}} '\{\{json .Config\}\}' {{conteneur}}`

- Affiche toutes les liaisons de port :

`docker inspect {{[-f|--format]}} '\{\{range $p, $conf := .NetworkSettings.Ports\}\} \{\{$p\}\} -> \{\{(index $conf 0).HostPort\}\} \{\{end\}\}' {{conteneur}}`

- Affiche l'aide :

`docker inspect`
