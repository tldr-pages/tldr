# docker exec

> Führe Befehle in einem bereits laufenden Docker Container aus.
> Weitere Informationen: <https://docs.docker.com/reference/cli/docker/container/exec/>.

- Öffne eine Shell innerhalb eines bereits laufenden Containers:

`docker exec {{[-it|--interactive --tty]}} {{container_name}} {{/bin/bash}}`

- Führe einen Befehl im Hintergrund (losgelöst) in einem laufenden Container aus:

`docker exec {{[-d|--detach]}} {{container_name}} {{befehl}}`

- Bestimme das Arbeitsverzeichnis, in dem der Befehl ausgeführt werden soll:

`docker exec {{[-it|--interactive --tty]}} {{[-w|--workdir]}} {{pfad/zu/verzeichnis}} {{container_name}} {{befehl}}`

- Führe einen Befehl im Hintergrund in einem laufenden Container aus, aber lies von der Standardeingabe:

`docker exec {{[-i|--interactive]}} {{[-d|--detach]}} {{container_name}} {{befehl}}`

- Setze eine Umgebungsvariable in einer laufenden Bash Sitzung:

`docker exec {{[-it|--interactive --tty]}} {{[-e|--env]}} {{variablen_name}}={{wert}} {{container_name}} {{/bin/bash}}`

- Führe einen Befehl als ein bestimmter Benutzer aus:

`docker exec {{[-u|--user]}} {{benutzer}} {{container_name}} {{befehl}}`
