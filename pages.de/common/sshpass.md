# sshpass

> Stelle SSH Passwörtern bereit.
> Weitere Informationen: <https://manned.org/sshpass>.

- Stelle eine Verbindung zu einem externen Server über ein Passwort aus einem Datei-Objekt her (in diesem Fall `stdin`):

`sshpass -d {{0}} ssh {{benutzer}}@{{server}}`

- Stelle eine Verbindung zu einem externen Server mit Hilfe eines Passworts bei automatischer Akzeptierung von unbekannten SSH Schlüsseln her:

`sshpass -p {{passwort}} ssh -o StrictHostKeyChecking=no {{benutzer}}@{{server}}`

- Stelle eine Verbindung zu einem externen Server mit Hilfe eines Passworts aus der ersten Zeile einer Datei bei automatischer Akzeptierung von unbekannten SSH Schlüsseln mit anschließender Ausführung eines Befehls her:

`sshpass -f {{pfad/zu/datei}} ssh -o StrictHostKeyChecking=no {{benutzer}}@{{server}} "{{befehl}}"`
