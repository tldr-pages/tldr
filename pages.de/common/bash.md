# bash

> Bourne-Again SHell.
> `sh`-kompatibler Kommandozeilen-Interpreter.
> Weitere Informationen: <https://gnu.org/software/bash/>.

- Interaktive Shell starten:

`bash`

- Führe einen Befehl aus:

`bash -c "{{befehl}}"`

- Führe Befehle aus einer Datei aus:

`bash {{pfad/zu/datei.sh}}`

- Führe Befehle aus einer Datei aus und protokolliere alle ausgeführten Befehle an das Terminal:

`bash -x {{pfad/zu/datei.sh}}`

- Führe Befehle aus einer Datei aus und stoppe beim ersten Fehler:

`bash -e {{pfad/zu/datei.sh}}`

- Führe Befehle von stdin aus:

`bash -s`

- Gib die Version von bash aus (verwende `echo $BASH_VERSION`, um nur die Versionszeichenkette anzuzeigen):

`bash --version`
