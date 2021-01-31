# sshpass

> Für die Bereitstellung von SSH Passwörtern.
> Es funktioniert über die Übergabe des Passwortes and ein temporäres TTY und die Weiterleitung des stdin an die SSH Sitzung.

- Verbindung zu einem externen Server über ein Passwort aus einem Datei-Objekt (in diesem Fall stdin):

`sshpass -d {{0}} ssh {{Benutzer}}@{{Server}}`

- Verbindung zu einem externen Server mit Hilfe eines Passworts bei automatischer Akzeptierung von unbekannten SSH Schlüsseln:

`sshpass -p {{Passwort}} ssh -o StrictHostKeyChecking=no {{Benutzer}}@{{Server}}`

- Verbindung zu einem externen Server mit Hilfe eines Passworts aus der ersten Zeile einer Datei bei automatischer Akzeptierung von unbekannten SSH Schlüsseln mit anschließender Ausführung eines Kommandos:

`sshpass -f {{Datei}} ssh -o StrictHostKeyChecking=no {{Benutzer}}@{{Server}} "{{Kommando}}"`
