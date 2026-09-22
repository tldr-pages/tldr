# docker image rm

> Verwijder Docker-images.
> Meer informatie: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Verwijder een of meer images op basis van hun namen:

`docker {{[rmi|image rm]}} {{image1 image2 ...}}`

- Forceer het verwijderen van een image:

`docker {{[rmi|image rm]}} {{[-f|--force]}} {{image}}`

- Verwijder een image zonder ongemerkte ouders te verwijderen:

`docker {{[rmi|image rm]}} --no-prune {{image}}`

- Toon de help:

`docker {{[rmi|image rm]}} --help`
