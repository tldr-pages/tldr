# choco pack

> Egy NuGet specifikáció csomagolása egy nupkg fájlba. További információ: <https://chocolatey.org/docs/commands-pack>.

- NuGet specifikáció csomagolása egy nupkg fájlba:

`choco pack {{path/to/specification}}`

- Csomagoljon egy NuGet specifikációt, megadva az eredményül kapott fájl verzióját:

`choco pack {{path/to/specification}} --version {{version}}`

- NuGet specifikáció csomagolása egy adott könyvtárba:

`choco pack {{path/to/specification}} --output-directory {{path/to/output_directory}}`
