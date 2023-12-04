# docker pull

> Télécharge une image docker depuis le registre.
> Plus d'informations : <https://docs.docker.com/engine/reference/commandline/pull/>.

- Télécharge une image docker spécifique :

`docker pull {{image}}:{{étiquette}}`

- Télécharge une image docker spécifique en mode silencieux :

`docker pull --quiet {{image}}:{{étiquette}}`

- Télécharge toutes les étiquettes d'une image docker spécifique :

`docker pull --all-tags {{image}}`

- Télécharge un image docker pour une plateforme spécifique, ex : linux/amd64 :

`docker pull --platform {{linux/amd64}} {{image}}:{{étiquette}}`

- Affiche l'aide :

`docker pull --help`
