# ssh-keygen

> Generiert ssh Schlüssel für Authentifizierung, Passwort-lose Logins und mehr.

- Interaktives Erstellen eines SSH Schlüssel-Paars:

`ssh-keygen`

- Erstellen eines Schlüssel-Paars unter einem bestimmten Dateinamen:

`ssh-keygen -f ~/.ssh/{{Dateiname}}`

- Generieren eines ed25519 Schlüssel-Paars mit 100 Schlüssel Ableitungs-Iterationen:

`ssh-keygen -t ed25519 -a 100`

- Generieren eines 4096 Bit langen RSA Schlüssel-Paars mit der Email im Kommentarfeld:

`ssh-keygen -t rsa -b 4096 -C "{{Email}}"`

- Abrufen des Schlüssel Fingerabdrucks von einem Server (hilfreich um die Authentizität eines Servers beim ersten Verbinden zu überprüfen):

`ssh-keygen -l -F {{Externer_Server}}`

- Entfernen der Schlüssel eines Servers aus der `known_hosts` Datei (hilfreich wenn ein Server seinen Schlüssel aktualisiert hat und der alte somit nicht mehr gilt):

`ssh-keygen -R {{Externer_Server}}`

- Abrufen des Fingerabdrucks eines Schlüssels im MD5 Hex Format:

`ssh-keygen -l -E md5 -f ~/.ssh/{{Dateiname}}`

- Ändern des Passworts eines privaten Schlüssels:

`ssh-keygen -p -f ~/.ssh/{{Dateiname}}`
