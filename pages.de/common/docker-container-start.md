# docker container start

> Starte einen oder mehrere gestoppte Container.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Starte einen Docker Container:

`docker {{[start|container start]}} {{container}}`

- Starte einen Container und verbinde dich mit der Standardausgabe sowie der Standardfehlerausgabe und leite Signale weiter:

`docker {{[start|container start]}} {{[-a|--attach]}} {{container}}`

- Starte einen oder mehrere durch Leerzeichen getrennte Container:

`docker {{[start|container start]}} {{container1 container2 ...}}`

- Zeige Hilfe:

`docker {{[start|container start]}} --help`
