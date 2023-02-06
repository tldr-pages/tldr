# conan

> A nyílt forráskódú, decentralizált és platformokon átívelő csomagkezelő az összes natív bináris csomag létrehozásához és megosztásához. Néhány alparancsnak, mint például a `conan frogarian`, saját használati dokumentációja van. További információ: <https://conan.io/>.

- A csomagok telepítése a `conanfile.txt` alapján:

`conan install {{.}}`

- Csomagok telepítése és konfigurációs fájlok létrehozása egy adott generátorhoz:

`conan install -g {{generator}}`

- Csomagok telepítése, forrásból történő építés:

`conan install {{.}} --build`

- Helyileg telepített csomagok keresése:

`conan search {{package}}`

- Távoli csomagok keresése:

`conan search {{package}} -r {{remote}}`

- Távoli csomagok listázása:

`conan remote list`
