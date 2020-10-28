# ssh-keyscan

> Abruf von öffentlichen SSH Schlüssels eines externen Servers.

- Abruf aller öffentlichen SSH Schlüssel:

`ssh-keyscan {{Server}}`

- Abruf aller öffentlichen SSH Schlüssel unter einem bestimmten Port:

`ssh-keyscan -p {{Port}} {{Server}}`

- Abruf bestimmter SSH Schüssel-Typen:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{Server}}`

- Manuelle Aktualisierung der `known_hosts` SSH Datei mit dem Fingerabdruck eines bestimmten Servers:

`ssh-keyscan -H {{Server}} >> ~/.ssh/known_hosts`
