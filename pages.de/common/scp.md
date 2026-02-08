# scp

> Sicheres Kopieren.
> Kopiere Dateien zwischen Hosts mit dem Secure Copy Protocol über SSH.
> Weitere Informationen: <https://man.openbsd.org/scp>.

- Kopiere eine lokale Datei zu einem Remote-Host:

`scp {{pfad/zu/lokale_datei}} {{remote_host}}:{{pfad/zu/remote_datei}}`

- Verwende einen bestimmten Port, wenn du dich mit dem Remote-Host verbindest:

`scp -P {{port}} {{pfad/zu/lokale_datei}} {{remote_host}}:{{pfad/zu/remote_datei}}`

- Kopiere eine Datei von einem Remote-Host in ein lokales Verzeichnis:

`scp {{remote_host}}:{{pfad/zu/remote_datei}} {{pfad/zu/lokal_verzeichnis}}`

- Kopiere rekursiv den Inhalt eines Verzeichnisses von einem Remote-Host in ein lokales Verzeichnis:

`scp -r {{remote_host}}:{{pfad/zu/remote_verzeichnis}} {{pfad/zu/lokal_verzeichnis}}`

- Kopiere eine Datei zwischen zwei Remote-Hosts und übertrage sie über den lokalen Host:

`scp -3 {{host1}}:{{pfad/zu/remote_datei}} {{host2}}:{{pfad/zu/remote_verzeichnis}}`

- Verwende einen bestimmten Benutzernamen, wenn du dich mit dem Remote-Host verbindest:

`scp {{pfad/zu/lokale_datei}} {{remote_benutzername}}@{{remote_host}}:{{pfad/zu/remote_verzeichnis}}`

- Verwende einen bestimmten SSH-Private Key für die Authentifizierung mit dem Remote-Host:

`scp -i {{~/.ssh/private_key}} {{pfad/zu/lokale_datei}} {{remote_host}}:{{pfad/zu/remote_datei}}`

- Verwende einen bestimmten Proxy, wenn du dich mit dem Remote-Host verbindest:

`scp -J {{proxy_benutzername}}@{{proxy_host}} {{pfad/zu/lokale_datei}} {{remote_host}}:{{pfad/zu/remote_datei}}`
