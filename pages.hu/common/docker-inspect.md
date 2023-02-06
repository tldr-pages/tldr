# docker inspect

> Docker objektumok alacsony szintű információinak visszaadása. További információ: <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Súgó megjelenítése:

`docker inspect`

- Információk megjelenítése egy konténerről, image-ről vagy kötetről egy név vagy ID segítségével:

`docker inspect {{container|image|ID}}`

- Egy konténer IP-címének megjelenítése:

`docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {{container}}`

- A konténer naplófájljának elérési útvonalának megjelenítése:

`docker inspect --format='{{.LogPath}}' {{container}}`

- A konténer képének nevének megjelenítése:

`docker inspect --format='{{.Config.Image}}' {{container}}`

- A konfigurációs információk megjelenítése JSON formátumban:

`docker inspect --format='{{json .Config}}' {{container}}`

- Az összes portkötés megjelenítése:

`docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' {{container}}`
