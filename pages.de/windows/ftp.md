# ftp

> Interaktiver Dateitransfer zwischen einem lokalen und einem entfernten FTP-Server.
> Weitere Informationen: <https://learn.microsoft.com/windows-server/administration/windows-commands/ftp>.

- Verbinden mit einem entfernten FTP-Server:

`ftp {{host}}`

- Anmelden als anonymer Benutzer:

`ftp -A {{host}}`

- Deaktivieren der automatische Anmeldung bei der ersten Verbindung:

`ftp -n {{host}}`

- Ausführen einer Datei, die eine Liste von FTP-Befehlen enthält:

`ftp -s:{{Pfad/zur/Datei}} {{host}}`

- Herunterladen von mehrerern Dateien (globaler Ausdruck):

`mget {{*.png}}`

- Hochladen von mehrerern Dateien (globaler Ausdruck):

`mput {{*.zip}}`

- Löschen mehrerer Dateien auf dem entfernten Server:

`mdelete {{*.txt}}`

- Ausführliche Hilfe anzeigen:

`ftp --help`
