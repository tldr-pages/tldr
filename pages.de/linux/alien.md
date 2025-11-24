# alien

> Ein Installations-Paket in ein anderes Format umwandeln.
> Weitere Informationen: <https://manned.org/alien>.

- Ein spezifisches Installationspaket in das Debian Format umwandeln (`.deb` Erweiterung):

`sudo alien {{[-d|--to-deb]}} {{pfad/zu/paket}}`

- Ein spezifisches Installationspaket in das Red Hat Format umwandeln (`.rpm` Erweiterung):

`sudo alien {{[-r|--to-rpm]}} {{pfad/zu/paket}}`

- Ein spezifisches Installationspaket in das Slackware Format umwandeln (`.tgz` Erweiterung):

`sudo alien {{[-t|--to-tgz]}} {{pfad/zu/paket}}`

- Ein spezifisches Installationspaket in das Debian Format umwandeln und auf dem System installieren:

`sudo alien {{[-d|--to-deb]}} --install {{pfad/zu/paket}}`
