# ssh-keygen

> Generiert ssh Schlüssel für Authentifizierung, Passwort-lose Logins und mehr.

- Erstelle ein SSH Schlüssel-Paar interaktiv:

`ssh-keygen`

- Erstelle ein Schlüssel-Paar unter einem bestimmten Dateinamen:

`ssh-keygen -f ~/.ssh/{{datei}}`

- Generiere ein ed25519 Schlüssel-Paar mit 100 Schlüssel-Ableitungs-Iterationen:

`ssh-keygen -t ed25519 -a 100`

- Generiere ein 4096 Bit langen RSA Schlüssel-Paar mit der Email im Kommentarfeld:

`ssh-keygen -t rsa -b 4096 -C "{{email}}"`

- Rufe den Schlüssel-Fingerabdruck von einem Server ab (hilfreich um die Authentizität eines Servers beim ersten Verbinden zu überprüfen):

`ssh-keygen -l -F {{externer_server}}`

- Entferne den Schlüssel eines Servers aus der `known_hosts` Datei (hilfreich wenn ein Server seinen Schlüssel aktualisiert hat und der alte somit nicht mehr gilt):

`ssh-keygen -R {{externer_server}}`

- Rufe den Fingerabdrucks eines Schlüssels im MD5 Hex Format ab:

`ssh-keygen -l -E md5 -f ~/.ssh/{{datei}}`

- Ändere das Passwort eines privaten Schlüssels:

`ssh-keygen -p -f ~/.ssh/{{datei}}`
