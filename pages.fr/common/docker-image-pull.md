# docker image pull

> Télécharge une image Docker depuis le registre.
> Plus d'informations : <https://docs.docker.com/reference/cli/docker/image/pull/>.

- Télécharge une image Docker spécifique :

`docker {{[pull|image pull]}} {{image}}:{{étiquette}}`

- Télécharge une image Docker spécifique en mode silencieux :

`docker {{[pull|image pull]}} {{[-q|--quiet]}} {{image}}:{{étiquette}}`

- Télécharge toutes les étiquettes d'une image Docker spécifique :

`docker {{[pull|image pull]}} {{[-a|--all-tags]}} {{image}}`

- Télécharge un image Docker pour une plateforme spécifique, ex : linux/amd64 :

`docker {{[pull|image pull]}} --platform {{linux/amd64}} {{image}}:{{étiquette}}`

- Affiche l'aide :

`docker {{[pull|image pull]}} {{[-h|--help]}}`
