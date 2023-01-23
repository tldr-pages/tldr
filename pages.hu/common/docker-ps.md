# docker ps

> Docker-konténerek listázása. További információ: <https://docs.docker.com/engine/reference/commandline/ps/>.

- Jelenleg futó docker konténerek listázása:

`docker ps`

- Az összes (futó és leállított) docker konténer listázása:

`docker ps --all`

- A legutóbb létrehozott konténer megjelenítése (minden állapotot tartalmaz):

`docker ps --latest`

- Szűrje azokat a konténereket, amelyek nevében szerepel egy részlánc:

`docker ps --filter="name={{name}}"`

- Szűrje azokat a konténereket, amelyeknek egy adott képen közös az őse:

`docker ps --filter "ancestor={{image}}:{{tag}}"`

- Konténerek szűrése kilépési állapotkód szerint:

`docker ps --all --filter="exited={{code}}"`

- Konténerek szűrése állapot szerint (létrehozott, futó, eltávolított, szüneteltetett, kilépett és halott):

`docker ps --filter="status={{status}}"`

- Olyan konténerek szűrése, amelyek egy adott kötetet csatlakoztatnak, vagy amelyek egy adott elérési útvonalra csatlakoztattak egy kötetet:

`docker ps --filter="volume={{path/to/directory}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
