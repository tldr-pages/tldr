# docker run

> Führe einen Befehl in einem neuen Docker Container aus.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/run/>.

- Führe einen Befehl in einem neuen Docker Container aus und verwende dabei einen bestimmten Tag eines Docker Images:

`docker run {{image:tag}} {{befehl}}`

- Führe einen Befehl in einem neuen Container im Hintergrund aus und zeige die ID:

`docker run {{[-d|--detach]}} {{image}} {{befehl}}`

- Führe einen Befehl in einem kurzlebigen Container im interaktiven Modus mit einem Pseudo-TTY aus:

`docker run --rm {{[-it|--interactive --tty]}} {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container mit übergebenen Umgebungsvariablen aus:

`docker run {{[-e|--env]}} '{{variable}}={{wert}}' {{[-e|--env]}} {{variable}} {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container mit eingebundenen Datenträgern aus:

`docker run {{[-v|--volume]}} {{pfad/zu/host_verzeichnis}}:{{pfad/zu/container_verzeichnis}} {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container mit veröffentlichten Ports aus:

`docker run {{[-p|--publish]}} {{host_port}}:{{container_port}} {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container aus und überschreibe den Einstiegspunkt des Images:

`docker run --entrypoint {{befehl}} {{image}}`

- Führe einen Befehl in einem neuen Container aus und verbinde ihn mit einem Netzwerk:

`docker run --network {{netzwerk}} {{image}}`
