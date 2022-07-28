# docker run

> Führe einen Befehl in einem neuen Docker Container aus.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/run/>.

- Führe einen Befehl in einem neuen Docker Container aus und verwende dabei einen bestimmten Tag eines Docker Images:

`docker run {{image:tag}} {{befehl}}`

- Führe einen Befehl in einem neuen Container im Hintergrund aus und zeige die ID:

`docker run --detach {{image}} {{befehl}}`

- Führe einen Befehl in einem kurzlebigen Container im interaktiven Modus mit einem Pseudo-TTY aus:

`docker run --rm --interactive --tty {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container mit übergebenen Umgebungsvariablen aus:

`docker run --env '{{variable}}={{wert}}' --env {{variable}} {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container mit eingebundenen Datenträgern aus:

`docker run --volume {{pfad/zu/host_verzeichnis}}:{{pfad/zu/container_verzeichnis}} {{image}} {{befehl}}`

- Führe einen Befehl in einem neuen Container mit veröffentlichten Ports aus:

`docker run --publish {{host_port}}:{{container_port}} {{image}} {{befehl}}`
