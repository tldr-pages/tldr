# alien

> Ein Installations-Paket in ein anderes Format umwandeln.
> Weitere Informationen: <https://manned.org/alien>.

- Ein spezifisches Installationspaket in das Debian Format umwandeln (`.deb` Erweiterung):

`sudo alien --to-deb {{pfad/zu/paket}}`

- Ein spezifisches Installationspaket in das Red Hat Format umwandeln (`.rpm` Erweiterung):

`sudo alien --to-rpm {{pfad/zu/paket}}`

- Ein spezifisches Installationspaket in das Slackware Format umwandeln (`.tgz` Erweiterung):

`sudo alien --to-tgz {{pfad/zu/paket}}`

- Ein spezifisches Installationspaket in das Debian Format umwandeln und auf dem System installieren:

`sudo alien --to-deb --install {{pfad/zu/paket}}`
