# docker image ls

> Toon Docker-images.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/image/ls/>.

- Alle Docker-images weergeven:

`docker {{[images|image ls]}}`

- Toon alle Docker-images inclusief tussenproducten:

`docker {{[images|image ls]}} {{[-a|--all]}}`

- Toon de uitvoer in stille modus (alleen numerieke ID's):

`docker {{[images|image ls]}} {{[-q|--quiet]}}`

- Toon alle Docker-images die door geen enkele container worden gebruikt:

`docker {{[images|image ls]}} {{[-f|--filter]}} dangling=true`

- Toon images die een substring in hun naam bevatten:

`docker {{[images|image ls]}} "{{*naam*}}"`

- Sorteer images op grootte:

`docker {{[images|image ls]}} --format "\{\{.ID\}\}\t\{\{.Size\}\}\t\{\{.Repository\}\}:\{\{.Tag\}\}" | sort {{[-k|--key]}} 2 {{[-h|--human-numeric-sort]}}`
