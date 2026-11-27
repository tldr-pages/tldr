# apt-mark

> Tool um den Status eines installierten Paketes zu verändern.
> Weitere Informationen: <https://manned.org/apt-mark>.

- Markiere ein Paket als automatisch installiert:

`sudo apt-mark auto {{paket}}`

- Halte ein Paket auf seiner aktuellen Version und verhindere dass es aktualisiert wird:

`sudo apt-mark hold {{paket}}`

- Erlaube dass ein Paket wieder aktualisiert werden darf:

`sudo apt-mark unhold {{paket}}`

- Zeige manuell installierte Pakete:

`apt-mark showmanual`

- Zeige gehaltene Pakete die nicht aktualisiert werden dürfen:

`apt-mark showhold`
