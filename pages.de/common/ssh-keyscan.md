# ssh-keyscan

> Rufe öffentliche SSH Schlüssel eines externen Servers ab.
> Weitere Informationen: <https://man.openbsd.org/ssh-keyscan>.

- Rufe alle öffentlichen SSH Schlüssel eines Servers ab:

`ssh-keyscan {{server}}`

- Rufe alle öffentlichen SSH Schlüssel unter einem bestimmten Port ab:

`ssh-keyscan -p {{port}} {{server}}`

- Rufe bestimmte SSH Schüssel-Typen ab:

`ssh-keyscan -t {{rsa,dsa,ecdsa,ed25519}} {{server}}`

- Aktualisiere die `known_hosts` SSH Datei mit dem Fingerabdruck eines bestimmten Servers:

`ssh-keyscan -H {{server}} >> ~/.ssh/known_hosts`
