# ssh-keygen

> Generiert ssh Schlüssel für Authentifizierung, Passwort-lose Logins und mehr.
> Weitere Informationen: <https://man.openbsd.org/ssh-keygen>.

- Erstelle ein SSH Schlüssel-Paar interaktiv:

`ssh-keygen`

- Erstelle ein Schlüssel-Paar unter einem bestimmten Dateinamen:

`ssh-keygen -f {{~/.ssh/datei}}`

- Generiere ein ed25519 Schlüssel-Paar mit 32 Schlüssel-Ableitungs-Iterationen:

`ssh-keygen -t {{ed25519}} -a {{32}}`

- Generiere ein 4096 Bit langen RSA Schlüssel-Paar mit der E-Mail im Kommentarfeld:

`ssh-keygen -t {{rsa}} -b {{4096}} -C "{{kommentar|e-mail}}"`

- Entferne den Schlüssel eines Servers aus der `known_hosts` Datei (hilfreich wenn ein Server seinen Schlüssel aktualisiert hat und der alte somit nicht mehr gilt):

`ssh-keygen -R {{externer_server}}`

- Rufe den Fingerabdruck eines Schlüssels im MD5 Hex Format ab:

`ssh-keygen -l -E {{md5}} -f {{~/.ssh/datei}}`

- Ändere das Passwort eines privaten Schlüssels:

`ssh-keygen -p -f {{~/.ssh/datei}}`

- Ändern Sie den Typ des Schlüsselformats (z. B. vom OPENSSH-Format in PEM), die Datei wird an Ort und Stelle neu geschrieben:

`ssh-keygen -p -N "" -m {{PEM}} -f ~/.ssh/{{datei}}`
