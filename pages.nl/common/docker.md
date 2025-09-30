# docker

> Beheer Docker containers en images.
> Sommige subcommando's zoals `run` hebben hun eigen documentatie.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/>.

- Toon alle Docker containers (actief en gestopte):

`docker ps {{[-a|--all]}}`

- Start een container van een image, met een aangepaste naam:

`docker run --name {{container_naam}} {{image}}`

- Start of stop een bestaande container:

`docker {{start|stop}} {{container_naam}}`

- Download een image uit een Docker register:

`docker pull {{image}}`

- Toon reeds gedownloade images:

`docker images`

- Open een interactieve tty met Bourne shell (`sh`) binnen een draaiende container:

`docker exec {{[-it|--interactive --tty]}} {{container_naam}} {{sh}}`

- Verwijder een gestopte container:

`docker rm {{container_naam}}`

- Vang en volg de logs van een container:

`docker logs {{[-f|--follow]}} {{container_naam}}`
