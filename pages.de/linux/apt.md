# apt

> Debian und Ubuntu Paket Management Tool.
> Empfohlene Alternative zu `apt-get` seit Ubuntu 16.04.
> Weitere Informationen: <https://manpages.debian.org/latest/apt/apt.8.html>.

- Aktualisiere die Liste der Paketquellen (es wird empfohlen, diesen Befehl zu Beginn auszuführen):

`sudo apt update`

- Suche nach einem Paket:

`apt search {{paket}}`

- Zeige Informationen über ein Paket:

`apt show {{paket}}`

- Installiere ein Paket oder aktualisiere es zur neusten Version:

`sudo apt install {{paket}}`

- Entferne ein Paket:

`sudo apt remove {{paket}}`

- Aktualisiere alle installierten Pakete auf die neueste Version:

`sudo apt upgrade`

- Liste alle Pakete auf:

`apt list`

- Liste alle installierten Pakete auf:

`apt list --installed`
