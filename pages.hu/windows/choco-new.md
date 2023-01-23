# choco new

> Új csomagspecifikációs fájlok generálása a Chocolatey segítségével. További információ: <https://chocolatey.org/docs/commands-new>.

- Új csomagváz létrehozása:

`choco new {{package_name}}`

- Új csomag létrehozása egy adott verzióval:

`choco new {{package_name}} --version {{version}}`

- Új csomag létrehozása egy adott karbantartó nevével:

`choco new {{package_name}} --maintainer {{maintainer_name}}`

- Új csomag létrehozása egy egyéni kimeneti könyvtárban:

`choco new {{package_name}} --output-directory {{path/to/directory}}`

- Új csomag létrehozása meghatározott 32 bites és 64 bites telepítő URL-címekkel:

`choco new {{package_name}} url="{{url}}" url64="{{url}}"`
