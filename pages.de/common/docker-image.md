# docker image

> Verwalte Docker Images.
> Siehe auch `docker build`, `docker import` und `docker pull`.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/image/>.

- Liste lokale Docker Images auf:

`docker image ls`

- Lösche nicht verwendete, lokale Docker Images:

`docker image prune`

- Lösche alle nicht verwendeten Docker Images (nicht nur die ohne Tag):

`docker image prune --all`

- Zeige die Geschichte eines lokalen Docker Images:

`docker image history {{image}}`
