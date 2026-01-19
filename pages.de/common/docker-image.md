# docker image

> Verwalte Docker Images.
> Siehe auch: `docker build`, `docker image pull`, `docker image rm`.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/image/>.

- Liste lokale Docker Images auf:

`docker {{[images|image ls]}}`

- Lösche nicht verwendete, lokale Docker Images:

`docker image prune`

- Lösche alle nicht verwendeten Docker Images (nicht nur die ohne Tag):

`docker image prune {{[-a|--all]}}`

- Zeige die Geschichte eines lokalen Docker Images:

`docker {{[history|image history]}} {{image}}`
