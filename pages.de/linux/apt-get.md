# apt-get

> Debian und Ubuntu Paket Management Tool.
> Suche mit `apt-cache` nach Paketen.
> Weitere Informationen: <https://manned.org/apt-get.8>.

- Aktualisiere die Liste der Paketquellen (es wird empfohlen diesen Befehl zu Beginn auszuführen):

`sudo apt-get update`

- Installiere ein Paket oder aktualisiere es zur neuesten Version:

`sudo apt-get install {{paket}}`

- Entferne ein Paket:

`sudo apt-get remove {{paket}}`

- Entferne ein Paket und die dazugehörigen Konfigurationen:

`sudo apt-get purge {{paket}}`

- Aktualisiere alle Pakete auf die neueste Version:

`sudo apt-get upgrade`

- Reinige das Repository:

`sudo apt-get autoclean`

- Entferne alle Pakete, die nicht mehr benötigt werden:

`sudo apt-get autoremove`

- Aktualisiere alle Pakete (wie `upgrade`), aber entfernt alle obsoleten Pakete:

`sudo apt-get dist-upgrade`
