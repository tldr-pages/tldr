# docker ps

> Liste Docker Container.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/ls/>.

- Liste zur Zeit laufende Container auf:

`docker ps`

- Liste laufende und gestoppte Container auf:

`docker ps {{[-a|--all]}}`

- Zeige den zuletzt erstellten Container (berücksichtigt jeden Status):

`docker ps {{[-l|--latest]}}`

- Zeige nur Container mit einer bestimmten Zeichenkette im Namen:

`docker ps {{[-f|--filter]}} "name={{name}}"`

- Zeige nur Container die von einem bestimmten Image abstammen:

`docker ps {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Zeige nur Container mit einem bestimmten Exit-Code:

`docker ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{code}}"`

- Zeige nur Container mit einem bestimmten Status (created, running, removing, paused, exited und dead):

`docker ps {{[-f|--filter]}} "status={{status}}"`

- Zeige nur Container, welche einen bestimmten Datenträger oder einen Datenträger an einem bestimmten Pfad eingehängt haben:

`docker ps {{[-f|--filter]}} "volume={{pfad/zu/verzeichnis}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
