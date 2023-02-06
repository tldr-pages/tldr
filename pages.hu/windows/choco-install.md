# choco install

> Egy vagy több csomag telepítése a Chocolatey segítségével. További információ: <https://chocolatey.org/docs/commands-install>.

- Telepítsen egy vagy több, szóközzel elválasztott csomagot:

`choco install {{package(s)}}`

- Csomagok telepítése egyéni konfigurációs fájlból:

`choco install {{path/to/packages.config}}`

- Egy adott nuspec vagy nupkg fájl telepítése:

`choco install {{path/to/file}}`

- Egy csomag egy adott verziójának telepítése:

`choco install {{package}} --version {{version}}`

- Egy csomag több verziójának telepítésének engedélyezése:

`choco install {{package}} --allow-multiple`

- Minden kérés automatikus megerősítése:

`choco install {{package}} --yes`

- Egyéni forrás megadása a csomagok fogadásához:

`choco install {{package}} --source {{source_url|alias}}`

- Felhasználónév és jelszó megadása a hitelesítéshez:

`choco install {{package}} --user {{username}} --password {{password}}`
