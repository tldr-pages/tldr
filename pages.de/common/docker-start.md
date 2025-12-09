# docker start

> Starte einen oder mehrere gestoppte Container.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/start/>.

- Zeige Hilfe:

`docker start`

- Starte einen Docker Container:

`docker start {{container}}`

- Starte einen Container und verbinde dich mit der Standardausgabe sowie der Standardfehlerausgabe und leite Signale weiter:

`docker start {{[-a|--attach]}} {{container}}`

- Starte einen oder mehrere durch Leerzeichen getrennte Container:

`docker start {{container1 container2 ...}}`
