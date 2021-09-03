# docker

> Verwalte Docker Container und Images.
> Manche Unterbefehle wie `docker run` sind separat dokumentiert.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Liste zur Zeit laufende Container auf:

`docker ps`

- Liste laufende und gestoppte Container auf:

`docker ps -a`

- Erzeuge einen Container aus einem Image und benenne ihn:

`docker run --name {{container_name}} {{pfad/zu/image}}`

- Stoppe oder starte einen existierenden Container:

`docker {{start|stop}} {{container_name}}`

- Lade ein Image herunter:

`docker pull {{pfad/zu/image}}`

- Öffne eine Konsole innerhalb eines bereits laufenden Containers:

`docker exec -it {{container_name}} {{sh}}`

- Lösche einen gestoppten Container:

`docker rm {{container_name}}`

- Zeige die Logs eines Containers an und aktualisiere sie automatisch:

`docker logs -f {{container_name}}`
