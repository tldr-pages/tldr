# apt

> Debian und Ubuntu Paket Management Tool..
> Empfohlene Alternative zu apt-get seit Ubuntu 16.04.

- Aktualisiert die Liste der Paketquellen (es wird empfohlen diesen Befehl als erstes auszuführen):

`sudo apt update`

- Sucht nach einem Paket:

`apt search {{Paket}}`

- Zeigt Informationen über ein Paket:

`apt show {{Paket}}`

- Installiert ein Paket oder aktualisiert es zur neusten Version:

`apt install {{Paket}}`

- Entfernt ein Paket:

`apt remove {{Paket}}`

- Entfernt ein Paket und die dazugehörigen Konfigurationen:

`apt purge {{Paket}}`

- Aktualisiert alle Pakete auf die neuste Version:

`apt upgrade`

- Listet alle Pakete:

`apt list`

- Listet alle installierten Pakete:

`apt list --installed`

- Reinigt das Repository - entfernt alle Dateinen (.deb) welche nichtmehr heruntergeladen werden können:

`apt autoclean`

- Entfernt alle Pakete welche nichtmehr benötigt werden:

`apt autoremove`

- Aktualisiert alle Pakete (wie `upgrade`), aber entfernt alle obsoleten Pakete:

`apt dist-upgrade`
