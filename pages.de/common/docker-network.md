# docker network

> Erzeuge und verwalte Docker Netzwerke.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/network/>.

- Liste alle verfügbaren und konfigurierten Docker Netzwerke auf:

`docker network ls`

- Erzeuge ein benutzerdefiniertes Netzwerk:

`docker network create --driver {{treiber_name}} {{netzwerk_name}}`

- Zeige detaillierte Informationen der mit Leerzeichen separierten Netzwerke an:

`docker network inspect {{netzwerk_name}}`

- Verbinde einen Container mit einem Netzwerk anhand des Namens oder der ID:

`docker network connect {{netzwerk_name}} {{container_name|ID}}`

- Trenne einen Container von einem Netzwerk:

`docker network disconnect {{netzwerk_name}} {{container_name|ID}}`

- Entferne alle unbenutzten (nicht von Containern referenzierten) Netzwerke:

`docker network prune`

- Entferne mehrere - durch Leerzeichen getrennte - Netzwerke:

`docker network rm {{netzwerk_name}}`
