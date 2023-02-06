# p7zip

> A 7-Zip fájlarchiváló nagy tömörítési aránnyal rendelkező csomagolója. Belsőleg vagy a 7za vagy a 7zr parancsot hajtja végre. További információ: <http://p7zip.sourceforge.net>.

- Archivál egy fájlt, kicserélve azt egy 7zippel tömörített változatra:

`p7zip {{path/to/file}}`

- Archivál egy fájlt, megtartva a bemeneti fájlt:

`p7zip -k {{path/to/file}}`

- Egy fájl kitömörítése, az eredeti tömörítetlen verzióval való helyettesítése:

`p7zip -d {{compressed.ext}}.7z`

- Egy fájl kicsomagolása a bemeneti fájl megtartásával:

`p7zip -d -k {{compressed.ext}}.7z`

- Néhány ellenőrzés kihagyása és a tömörítés vagy a tömörítés kikényszerítése:

`p7zip -f {{path/to/file}}`
