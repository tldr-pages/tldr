# docker inspect

> Retour d'informations de bas niveau sur les objets Docker.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Montrer l'aide

`docker inspect`

- Afficher les informations de configuration d'un conteneur, image ou volume en utilisant un nom ou un ID :

`docker inspect {{conteneur|image|ID}}`

- Afficher l'adresse IP d'un conteneur :

`docker inspect --format='{{range .NetworkSettings.Networks}} {{.IPAddress}}{{end}}' {{conteneur}}`

- Afficher le chemin du fichier journal d'un conteneur :

`docker inspect --format='{{.LogPath}}' {{conteneur}}`

- Afficher le nom de l'image d'un conteneur :

`docker inspect --format='{{.Config.Image}}' {{conteneur}}`

- Afficher les informations de configuration en JSON :

`docker inspect --format='{{json .Config}}' {{conteneur}}`

- Afficher toutes les liaisons de port :

`docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' {{conteneur}}`
