# docker

> Verwalte Docker Container und Images.
> Manche Unterbefehle wie `run` sind separat dokumentiert.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/>.

- Liste laufende und gestoppte Container auf:

`docker ps {{[-a|--all]}}`

- Erzeuge einen Container aus einem Image und benenne ihn:

`docker run --name {{container_name}} {{image}}`

- Stoppe oder starte einen existierenden Container:

`docker {{start|stop}} {{container_name}}`

- Lade ein Image herunter:

`docker pull {{image}}`

- Zeige eine Liste der bereits heruntergeladenen Images an:

`docker images`

- Öffne eine Konsole innerhalb eines bereits laufenden Containers:

`docker exec {{[-it|--interactive --tty]}} {{container_name}} {{sh}}`

- Lösche einen gestoppten Container:

`docker rm {{container_name}}`

- Zeige die Logs eines Containers an und aktualisiere sie automatisch:

`docker logs {{[-f|--follow]}} {{container_name}}`
