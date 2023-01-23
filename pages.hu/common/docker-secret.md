# docker secret

> Docker swarm titkok kezelése. További információ: <https://docs.docker.com/engine/reference/commandline/secret/>.

- Hozzon létre egy új titkot a `stdin` oldalon:

`{{command}} | docker secret create {{secret_name}} -`

- Új titok létrehozása egy fájlból:

`docker secret create {{secret_name}} {{path/to/file}}`

- Az összes titok listázása:

`docker secret ls`

- Egy vagy több titok részletes információinak megjelenítése emberbarát formátumban:

`docker secret inspect --pretty {{secret_name1 secret_name2 ...}}`

- Egy vagy több titok eltávolítása:

`docker secret rm {{secret_name1 secret_name2 ...}}`
