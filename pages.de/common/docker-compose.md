# docker-compose

> Starte und Verwalte Docker Applikationen bestehend aus mehreren Containern.
> Weitere Informationen: <https://docs.docker.com/compose/reference/overview/>.

- Liste zur Zeit laufende Container auf:

`docker-compose ps`

- Erzeuge und starte alle Container im Hintergrund unter der Verwendung der Datei `docker-compose.yml` im aktuellen Verzeichnis:

`docker-compose up -d`

- Starte alle Container und baue diese neu, wenn nötig:

`docker-compose up --build`

- Starte alle Container unter der Verwendung einer alternativen Compose Datei:

`docker-compose --file {{pfad/zu/verzeichnis}} up`

- Stoppe alle laufenden Container:

`docker-compose stop`

- Stoppe und lösche alle Container, Netzwerke, Images und Volumes:

`docker-compose down --rmi all --volumes`

- Zeige die Logs aller Container an und aktualisiere sie automatisch:

`docker-compose logs --follow`

- Zeige die Logs eines bestimmten Containers an und aktualisiere sie automatisch:

`docker-compose logs --follow {{container_name}}`
