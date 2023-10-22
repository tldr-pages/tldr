# apt-cache

> Debian und Ubuntu-Paketsuche.
> Weitere Informationen: <https://manpages.debian.org/latest/apt/apt-cache.8.html>.

- Suche nach einem Paket in deinen aktuellen Paketquellen:

`apt-cache search {{suchbegriff}}`

- Zeige die Paketinformationen zu einem Paket:

`apt-cache show {{paket}}`

- Überprüfe ob ein Paket installiert und up to date ist:

`apt-cache policy {{paket}}`

- Zeige die Abhängigkeiten eines Pakets:

`apt-cache depends {{paket}}`

- Zeige Pakete die von einem bestimmten Paket abhängen:

`apt-cache rdepends {{paket}}`
