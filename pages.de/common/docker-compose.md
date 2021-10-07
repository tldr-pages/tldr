# docker-compose

> Starte und verwalte Docker Applikationen bestehend aus mehreren Containern.
> Weitere Informationen: <https://docs.docker.com/compose/reference/overview/>.

- Liste zur Zeit laufende Container auf:

`docker-compose ps`

- Erzeuge und starte alle Container im Hintergrund unter der Verwendung der Datei `docker-compose.yml` im aktuellen Verzeichnis:

`docker-compose up -d`

- Starte alle Container und baue sie neu, wenn nötig:

`docker-compose up --build`

- Starte alle Container unter der Verwendung einer alternativen Compose Datei:

`docker-compose --file {{pfad/zu/verzeichnis}} up`

- Stoppe alle laufenden Container:

`docker-compose stop`

- Stoppe und lösche alle Container, Netzwerke, Images und Volumes:

`docker-compose down --rmi all --volumes`

- Zeige die Logs aller Container kontinuierlich an:

`docker-compose logs --follow`

- Zeige die Logs eines spezifischen Containers kontinuierlich an:

`docker-compose logs --follow {{container_name}}`
