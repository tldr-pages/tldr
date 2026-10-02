# podman ps

> Toon Podman-containers.
> Meer informatie: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- Toon momenteel draaiende Podman-containers:

`podman ps`

- Toon alle Podman-containers (actief en gestopt):

`podman ps {{[-a|--all]}}`

- Toon de laatst aangemaakte container (inclusief alle toestanden):

`podman ps {{[-l|--latest]}}`

- Filter containers die een substring in hun naam bevatten:

`podman ps {{[-f|--filter]}} "name={{naam}}"`

- Filter containers die een bepaalde image als voorouder hebben:

`podman ps {{[-f|--filter]}} "ancestor={{image}}:{{tag}}"`

- Filter containers op exitstatuscode:

`podman ps {{[-a|--all]}} {{[-f|--filter]}} "exited={{code}}"`

- Filter containers op status:

`podman ps {{[-f|--filter]}} "status={{created|running|removing|paused|exited|dead}}"`

- Filter containers die een specifiek volume koppelen of waarvan het volume op een specifiek pad is gekoppeld:

`podman ps {{[-f|--filter]}} "volume={{pad/naar/map}}" --format "table \{\{.ID\}\}\t\{\{.Image\}\}\t\{\{.Names\}\}\t\{\{.Mounts\}\}"`
