# docker volume

> Docker kötetek kezelése. További információ: <https://docs.docker.com/engine/reference/commandline/volume/>.

- Hozzon létre egy kötetet:

`docker volume create {{volume_name}}`

- Létrehoz egy kötetet egy adott címkével:

`docker volume create --label {{label}} {{volume_name}}`

- Hozzon létre egy `tmpfs` kötetet 100 MiB méretű és 1000-es uiddel:

`docker volume create --opt {{type}}={{tmpfs}} --opt {{device}}={{tmpfs}} --opt {{o}}={{size=100m,uid=1000}} {{volume_name}}`

- Listázza ki az összes kötetet:

`docker volume ls`

- Egy kötet eltávolítása:

`docker volume rm {{volume_name}}`

- A kötetre vonatkozó információk megjelenítése:

`docker volume inspect {{volume_name}}`

- Az összes nem használt helyi kötet eltávolítása:

`docker volume prune`

- Súgó megjelenítése egy alparancshoz:

`docker volume {{subcommand}} --help`
