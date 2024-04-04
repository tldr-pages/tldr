# docker

> Beheer Docker containers en images.
> Sommige subcommando's zoals `docker run` hebben hun eigen documentatie.
> Meer informatie: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Toon alle Docker containers (actief en gestopte):

`docker ps --all`

- Start een container van een image, met een aangepaste naam:

`docker run --name {{container_naam}} {{image}}`

- Start of stop een bestaande container:

`docker {{start|stop}} {{container_naam}}`

- Download een image uit een Docker register:

`docker pull {{image}}`

- Toon reeds gedownloade images:

`docker images`

- Open een shell in een actieve container:

`docker exec -it {{container_naam}} {{sh}}`

- Verwijder een gestopte container:

`docker rm {{container_naam}}`

- Volg de logs van een container:

`docker logs -f {{container_naam}}`
