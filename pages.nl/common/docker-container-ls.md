# docker container ls

> Toon Docker-containers.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Toon momenteel draaiende Docker-containers:

`docker {{[ps|container ls]}}`

- Toon alle Docker-containers (actief en gestopt):

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Toon de laatst aangemaakte container (inclusief alle toestanden):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Filter containers die een substring in hun naam bevatten:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{naam}}"`

- Filter containers die een bepaalde afbeelding als voorouder hebben:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Filter containers op exit-statuscode:

`docker {{[ps|container ls]}} {{[-a|--all]}} {{[-f|--filter]}} "exited={{code}}"`

- Filter containers op status (created, running, removing, paused, exited en dead):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{status}}"`

- Filter containers die gekoppeld zijn aan een specifiek volume of waarvan het volume op een specifiek pad is gekoppeld:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{pad/naar/map}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
