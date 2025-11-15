# docker rmi

> Lösche eines oder mehrere Docker Images.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/image/rm/>.

- Zeige Hilfe:

`docker rmi`

- Lösche eines oder mehrere Docker Images anhand der angegebenen Namen:

`docker rmi {{image1 image2 ...}}`

- Erzwinge das Löschen eines Images:

`docker rmi {{[-f|--force]}} {{image}}`

- Lösche ein Image aber behalte Eltern-Images ohne Tag:

`docker rmi --no-prune {{image}}`
