# apt-get

> Debian und Ubuntu Paket Management Tool.
> Suche mit `apt-cache` nach Paketen.

- Aktualisiert die Liste der Paketquellen (es wird empfohlen diesen Befehl als erstes auszuführen):

`apt-get update`

- Installiert ein Paket oder aktualisiert es zur neusten Version:

`apt-get install {{Paket}}`

- Entfernt ein Paket:

`apt-get remove {{Paket}}`

- Entfernt ein Paket und die dazugehörigen Konfigurationen:

`apt-get purge {{Paket}}`

- Aktualisiert alle Pakete auf die neuste Version:

`apt-get upgrade`

- Reinigt das Repository - entfernt alle Dateinen (`.deb`) welche nichtmehr heruntergeladen werden können:

`apt-get autoclean`

- Entfernt alle Pakete welche nichtmehr benötigt werden:

`apt-get autoremove`

- Aktualisiert alle Pakete (wie `upgrade`), aber entfernt alle obsoleten Pakete:

`apt-get dist-upgrade`
