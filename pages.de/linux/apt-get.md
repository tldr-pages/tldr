# apt-get

> Debian und Ubuntu Paket Management Tool.
> Suche mit `apt-cache` nach Paketen.
> Mehr Informationen: <https://manpages.debian.org/latest/apt/apt-get.8.en.html>.

- Aktualisiere die Liste der Paketquellen (es wird empfohlen diesen Befehl zu Begin auszuführen):

`apt-get update`

- Installiere ein Paket oder aktualisiere es zur neusten Version:

`apt-get install {{paket}}`

- Entferne ein Paket:

`apt-get remove {{paket}}`

- Entferne ein Paket und die dazugehörigen Konfigurationen:

`apt-get purge {{paket}}`

- Aktualisiere alle Pakete auf die neuste Version:

`apt-get upgrade`

- Reinige das Repository

`apt-get autoclean`

- Entferne alle Pakete, die nicht mehr benötigt werden:

`apt-get autoremove`

- Aktualisiere alle Pakete (wie `upgrade`), aber entfernt alle obsoleten Pakete:

`apt-get dist-upgrade`
