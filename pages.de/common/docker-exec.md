# docker exec

> Führe Befehle in einem bereits laufenden Docker Container aus:
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/exec/>.

- Öffne eine Konsole innerhalb eines bereits laufenden Containers:

`docker exec --interactive --tty {{container_name}} {{/bin/bash}}`

- Führe einen Befehl im Hintegrund (losgelöst) in einem laufenden Container aus:

`docker exec --detach {{container_name}} {{befehl}}`

- Bestimme das Arbeitsverzeichnis, in welchem der Befehl ausgeführt werden soll:

`docker exec --interactive -tty --workdir {{pfad/zum/verzeichnis}} {{container_name}} {{befehl}}`

- Führe einen Befehl im Hintergrund in einem laufenden Container aus, aber erhalte die Ausgabe:

`docker exec --interactive --detach {{container_name}} {{befehl}}`

- Setze eine Umgebungsvariable in einer laufenden Bash Sitzung:

`docker exec --interactive --tty --env {{variablen_name}}={{wert}} {{container_name}} {{/bin/bash}}`

- Führe einen Befehl als ein bestimmter Benutzer aus:

`docker exec --user {{benutzer}} {{container_name}} {{befehl}}`
