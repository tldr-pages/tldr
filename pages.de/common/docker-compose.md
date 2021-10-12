# docker-compose

> Starte und verwalte Anwendungen, welche aus mehreren Docker Containern bestehen. Für alle Befehle werden standardmäßig Containerdefinitionen aus der `docker-compose.yml` Datei im aktuellen Arbeitsverzeichnis ausgelesen.
> Weitere Informationen: <https://docs.docker.com/compose/reference/>.

- Liste alle laufenden Container auf:

`docker-compose ps`

- Erstelle alle Container und starte diese im Hintergrund:

`docker-compose up -d`

- Starte alle Container. Erzeuge zugehörige Docker Images bei Bedarf neu.

`docker-compose up --build`

- Starte alle Container für eine alternative docker-compose Datei:

`docker-compose --file {{Pfad/zur/Datei}} up`

- Stoppe alle laufenden Container:

`docker-compose stop`

- Stoppe und entferne alle Container inklusive zugehöriger Netzwerke, Volumes und Images:

`docker-compose down --rmi all --volumes`

- Zeige Log-Nachrichten aller laufender Container inklusive Zeitstempel an:

`docker-compose logs -t`

- Zeige aktuelle Log-Nachrichten laufender Container an:

`docker-compose logs --follow`

- Zeige aktuelle Log-Nachrichten eines spezifischen Containers an:

`docker-compose logs --follow {{Name_des_Containers}}`
