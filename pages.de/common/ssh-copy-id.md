# ssh-copy-id

> Installiere den öffentlichen Teil eines SSH Schlüssels in der `authorized_keys` Datei auf einem externen Server.
> Weitere Informationen: <https://manned.org/ssh-copy-id>.

- Kopiere den eigenen öffentlichen SSH Schlüssels zu einem externen Server:

`ssh-copy-id {{benutzer}}@{{externer_server}}`

- Kopiere den angegebenen öffentlichen SSH Schlüssels zu einem externen Server:

`ssh-copy-id -i {{pfad/zu/öffentlichem_schlüssel}} {{benutzer}}@{{externer_server}}`

- Kopiere den angegeben öffentlichen SSH Schlüssels zu einem externen Server unter Angabe eines bestimmten SSH Ports:

`ssh-copy-id -i {{pfad/zu/öffentlichem_schlüssel}} -p {{port}} {{benutzer}}@{{externer_server}}`
