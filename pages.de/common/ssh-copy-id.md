# ssh-copy-id

> Installiert den öffentlichen Teil eines SSH Schlüssels in der `authorized_keys` Datei eines Benutzers von einem externen Server.
> Ermöglicht darüber das zukünftige Einloggen unter diesem Benutzernamen bei diesem Server mit diesem Schlüssel.

- Kopieren des eigenen öffentlichen SSH Schlüssels zu einem externen Server:

`ssh-copy-id {{Benutzer@Externer_Server}}`

- Kopieren des angegebenen öffentlichen SSH Schlüssels zu einem externen Server:

`ssh-copy-id -i {{Pfad/zum/öffentlichen/Schlüssel}} {{Benutzer}}@{{Externer_Server}}`

- Kopieren des angegeben öffentlichen SSH Schlüssels zu einem externen Server unter Angabe eines bestimmten SSH Ports:

`ssh-copy-id -i {{Pfad/zum/öffentlichen/Schlüssel}} -p {{port}} {{Benutzer}}@{{Externer_Server}}`
