# docker

> Beheer Docker containers en images.
> Sommige subcommando's zoals `docker run` hebben hun eigen documentatie.
> Meer informatie: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Maak een lijst van alle docker containers (actief en gestopte):

`docker ps --all`

- Start een container van een image, met een aangepaste naam:

`docker run --name {{container_naam}} {{image}}`

- Start of stop een bestaande container:

`docker {{start|stop}} {{container_naam}}`

- Haal een image op uit een docker register:

`docker pull {{image}}`

- Geef een lijst met reeds gedownloade images weer:

`docker images`

- Open een shell in een actieve container:

`docker exec -it {{container_naam}} {{sh}}`

- Verwijder een gestopte container:

`docker rm {{container_naam}}`

- Haal en volg de logs van een container:

`docker logs -f {{container_naam}}`
