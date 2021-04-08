# apt

> Debian und Ubuntu Paket Management Tool.
> Empfohlene Alternative zu apt-get seit Ubuntu 16.04.
> Mehr Informationen: <https://manned.org/apt.8>.

- Aktualisiere die Liste der Paketquellen (es wird empfohlen diesen Befehl zu Begin auszuführen):

`sudo apt update`

- Suche nach einem Paket:

`apt search {{paket}}`

- Zeige Informationen über ein Paket:

`apt show {{paket}}`

- Installiere ein Paket oder aktualisiere es zur neusten Version:

`sudo apt install {{paket}}`

- Entferne ein Paket:

`sudo apt remove {{paket}}`

- Liste alle Pakete auf:

`apt list`

- Liste alle installierten Pakete auf:

`apt list --installed`
