# docker compose

> Starte und verwalte Anwendungen, welche aus mehreren Docker Containern bestehen.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/compose/>.

- Liste alle laufenden Container auf:

`docker compose ps`

- Erzeuge und starte alle Container im Hintergrund unter der Verwendung der Datei `docker-compose.yml` im aktuellen Verzeichnis:

`docker compose up {{[-d|--detach]}}`

- Starte alle Container. Erzeuge zugehörige Docker Images bei Bedarf neu:

`docker compose up --build`

- Starte alle Container durch Angabe eines Projektnamens unter Verwendung einer alternativen Compose-Datei:

`docker compose {{[-p|--project-name]}} {{Projektname}} {{[-f|--file]}} {{pfad/zu/verzeichnis}} up`

- Stoppe alle laufenden Container:

`docker compose stop`

- Stoppe und entferne alle Container inklusive zugehöriger Netzwerke, Volumes und Images:

`docker compose down --rmi all {{[-v|--volumes]}}`

- Zeige die Logs aller Container kontinuierlich an:

`docker compose logs {{[-f|--follow]}}`

- Zeige die Logs eines spezifischen Containers kontinuierlich an:

`docker compose logs {{[-f|--follow]}} {{container_name}}`
