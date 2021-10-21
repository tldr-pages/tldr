# docker run

> Führe einen Befehl in einem neuen Docker Container aus.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/run/>.

- Führe einen Befehl in einem neuen Docker Container aus und verwende dabei einen bestimmten Tag eines Docker Images:

`docker run {{image:tag}} {{befehl}}`

- Führe einen Befehl in einem neuen Container im Hintergrund aus und zeige die ID:

`docker run -d {{image}} {{befehl}}`

- Führe einen Befehl in einem kurzlebigen Container im interaktiven Modus mit einem Pseudo-TTY aus:

`docker run --rm -it {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container mit übergebenen Umgebungsvariablen aus:

`docker run -e '{{variable}}={{wert}}' -e {{variable}} {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container mit eingebundenen Datenträgern aus:

`docker run -v {{pfad/zu/host_verzeichnis}}:{{pfad/zu/container_verzeichnis}} {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container mit veröffentlichten Ports aus:

`docker run -p {{host_port}}:{{container_port}} {{image}} {{befehl}}`
