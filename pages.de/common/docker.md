# docker

> Zum Verwalten von Docker Containern und Images.
> Mehr Informationen: <https://docs.docker.com/engine/reference/commandline/cli/>.

- Zur Zeit laufende Container auflisten:

`docker ps`

- Alle Container auflisten (laufende und gestoppte):

`docker ps -a`

- Erzeuge einen Container aus einem Image und benenne ihn:

`docker run --name {{container_name}} {{image}}`

- Einen existierenden Container starten oder stoppen:

`docker {{start|stop}} {{container_name}}`

- Ein Image herunterladen:

`docker pull {{image}}`

- Eine Konsole innerhalb eines bereits laufenden Containers öffnen:

`docker exec -it {{container_name}} {{sh}}`

- Einen gestoppten Container löschen:

`docker rm {{container_name}}`

- Die Logs eines Containers anzeigen und automatisch aktualisieren:

`docker logs -f {{container_name}}`
