# docker container ls

> Liste Docker Container.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Liste zur Zeit laufende Container auf:

`docker {{[ps|container ls]}}`

- Liste laufende und gestoppte Container auf:

`docker {{[ps|container ls]}} {{[-a|--all]}}`

- Zeige den zuletzt erstellten Container (berücksichtigt jeden Status):

`docker {{[ps|container ls]}} {{[-l|--latest]}}`

- Zeige nur Container mit einer bestimmten Zeichenkette im Namen:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "name={{name}}"`

- Zeige nur Container die von einem bestimmten Image abstammen:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Zeige nur Container mit einem bestimmten Exit-Code:

`docker {{[ps|container ls]}} {{[-a|--all]}} {{[-f|--filter]}} "exited={{code}}"`

- Zeige nur Container mit einem bestimmten Status (created, running, removing, paused, exited und dead):

`docker {{[ps|container ls]}} {{[-f|--filter]}} "status={{status}}"`

- Zeige nur Container, welche einen bestimmten Datenträger oder einen Datenträger an einem bestimmten Pfad eingehängt haben:

`docker {{[ps|container ls]}} {{[-f|--filter]}} "volume={{pfad/zu/verzeichnis}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
