# podman

> Egyszerű menedzsment eszköz podok, konténerek és image-ek számára. A Podman Docker-CLI-hez hasonló parancssoros eszközt biztosít. Egyszerűen megfogalmazva: `alias docker=podman`. További információ: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- Az összes konténer (futó és leállított) listázása:

`podman ps --all`

- Konténer létrehozása egy képből, egyéni névvel:

`podman run --name {{container_name}} {{image}}`

- Egy meglévő konténer elindítása vagy leállítása:

`podman {{start|stop}} {{container_name}}`

- Képet húz egy nyilvántartóból (alapértelmezett a Docker Hub):

`podman pull {{image}}`

- A már letöltött image-ek listájának megjelenítése:

`podman images`

- Héj megnyitása egy már futó konténeren belül:

`podman exec --interactive --tty {{container_name}} {{sh}}`

- Egy leállított konténer eltávolítása:

`podman rm {{container_name}}`

- Egy vagy több konténer naplóinak megjelenítése és a naplókimenetek követése:

`podman logs --follow {{container_name}} {{container_id}}`
