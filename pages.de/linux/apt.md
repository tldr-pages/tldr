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

`sudo apt install {{Paket}}`

- Entfernt ein Paket:

`sudo apt remove {{Paket}}`

- Listet alle Pakete:

`apt list`

- Listet alle installierten Pakete:

`apt list --installed`
