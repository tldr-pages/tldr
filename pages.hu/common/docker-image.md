# docker image

> Docker-képek kezelése. Lásd még: `docker build`, `docker import` és `docker pull`. További információ: <https://docs.docker.com/engine/reference/commandline/image/>.

- Helyi Docker-képek listázása:

`docker image ls`

- A nem használt helyi Docker-képek törlése:

`docker image prune`

- Az összes nem használt kép törlése (nem csak a címke nélkülieké):

`docker image prune --all`

- A helyi Docker-képek előzményeinek megjelenítése:

`docker image history {{image}}`
