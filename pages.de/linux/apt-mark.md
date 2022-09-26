# apt-mark

> Tool um den Status eines installierten Paketes zu verändern.
> Weitere Informationen: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Markiere ein Paket als automatisch installiert:

`sudo apt-mark auto {{paketname}}`

- Halte ein Paket auf seiner aktuellen Version und verhindere dass es aktualisiert wird:

`sudo apt-mark hold {{paketname}}`

- Erlaube dass ein Paket wieder aktualisiert werden darf:

`sudo apt-mark unhold {{paketname}}`

- Zeige manuell installierte Pakete:

`apt-mark showmanual`

- Zeige gehaltene Pakete die nicht aktualisiert werden dürfen:

`apt-mark showhold`
