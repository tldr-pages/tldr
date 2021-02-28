# bash

> Bourne-Again SHell.
> `sh`-kompatibler Kommandozeilen-Interpreter.
> Mehr Informationen: <https://gnu.org/software/bash>.

- Interaktive Shell starten:

`bash`

- Führe einen Befehl aus:

`bash -c "{{befehl}}"`

- Befehle aus einer Datei ausführen:

`bash {{datei.sh}}`

- Ausführen von Befehlen aus einer Datei, Protokollierung aller ausgeführten Befehle an das Terminal:

`bash -x {{datei.sh}}`

- Führe Befehle aus einer Datei aus und stoppen Sie beim ersten Fehler:

`bash -e {{datei.sh}}`

- Befehle von stdin ausführen:

`bash -s`

- Drucke die Versionsinformationen der bash aus (verwende `echo $BASH_VERSION`, um nur die Versionszeichenkette anzuzeigen):

`bash --version`
