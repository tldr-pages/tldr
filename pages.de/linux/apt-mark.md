# apt-mark

> Tool um den Status eines installierten Paketes zu verändern.
> Mehr Informationen: <https://manpages.debian.org/latest/apt/apt-mark.8.html>.

- Markiere ein Paket als automatisch installiert:

`sudo apt-mark auto {{paket_name}}`

- Halte ein Paket auf seiner aktuellen Version und verhindere dass es aktualisiert wird:

`sudo apt-mark hold {{paket_name}}`

- Erlaube dass ein Paket wieder aktualisiert werden darf:

`sudo apt-mark unhold {{package_name}}`

- Zeige manuell installierte Pakete:

`apt-mark showmanual`

- Zeige gehaltene Pakete die nicht aktualisiert werden dürfen:

`apt-mark showhold`
