# ssh

> Secure Shell ist ein Protokoll für das sichere einloggen auf einem externen System.
> Es kann dadurch eingesetzt werden um Kommandos auf externen Systemen auszuführen.

- Verbindung zu einem externen Server:

`ssh {{Benutzer}}@{{Externer_Server}}`

- Verbindung zu einem externen Server mit spezifischer Identität (privatem SSH Schlüssel):

`ssh -i {{path/to/key_file}} {{Benutzer}}@{{Externer_Server}}`

- Verbindung zu einem externen Server unter einem spezifischen Port:

`ssh {{Benutzer}}@{{Externer_Server}} -p {{2222}}`

- Ausführen eines Kommandos auf einem externen Server:

`ssh {{Externer_Server}} {{Kommando -mit -Optionen}}`

- SSH Tunneln: Dynamische Port Weiterleitung (SOCKS proxy auf localhost:9999):

`ssh -D {{9999}} -C {{Benutzer}}@{{Externer_Server}}`

- SSH Tunneln: Weiterleitung eines spezifischen Ports (localhost:9999 zu example.org:80) zusammen mit deaktivierter pseudy-tty Provisionierung für die Ausführung eines Befehls:

`ssh -L {{9999}}:{{example.org}}:{{80}} -N -T {{Benutzer}}@{{Externer_Server}}`

- SSH Springen: Verbinden über einen Spring-Server zu einem externen Server (Es können auch mehrere Spring-Server über eine Komma-separierte Liste angegeben werden):

`ssh -J {{Benutzer}}@{{Spring_Server}} {{Benutzer}}@{{Externer_Server}}`

- Agenten Weiterleitung: Weiterleiten der eigenen Authentifizierungs-Information an den externen Server (siehe `man ssh_config` für mehr Optionen):

`ssh -A {{Benutzer}}@{{Externer_Server}}`
