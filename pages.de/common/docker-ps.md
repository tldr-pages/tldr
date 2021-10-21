# docker ps

> Liste Docker Container.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/ps/>.

- Liste zur Zeit laufende Container auf:

`docker ps`

- Liste laufende und gestoppte Container auf:

`docker ps --all`

- Zeige den zuletzt erstellten Container (berücksichtigt jeden Status):

`docker ps --latest`

- Zeige nur Container mit einer bestimmten Zeichenkette im Namen:

`docker ps --filter="name={{name}}"`

- Zeige nur Container die von einem bestimmten Image abstammen:

`docker ps --filter "ancestor={{image}}:{{tag}}"`

- Zeige nur Container mit einem bestimmten Exit-Code:

`docker ps --all --filter="exited={{code}}"`

- Zeige nur Container mit einem bestimmten Status (created, running, removing, paused, exited und dead):

`docker ps --filter="status={{status}}"`

- Zeige nur Container, welche einen bestimmten Datenträger oder einen Datenträger an einem bestimmten Pfad eingehängt haben:

`docker ps --filter="volume={{pfad/zum/verzeichnis}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
