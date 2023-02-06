# docker rmi

> Egy vagy több Docker-kép eltávolítása. További információ: <https://docs.docker.com/engine/reference/commandline/rmi/>.

- Segítség megjelenítése:

`docker rmi`

- Egy vagy több kép eltávolítása a nevük alapján:

`docker rmi {{image1 image2 ...}}`

- Egy kép eltávolításának kikényszerítése:

`docker rmi --force {{image}}`

- Egy kép eltávolítása a címkézetlen szülők törlése nélkül:

`docker rmi --no-prune {{image}}`
