# yaa

> Maak en beheer YAA-archieven.
> Meer informatie: <https://keith.github.io/xcode-man-pages/yaa.1.html>.

- Maak een archief van een map:

`yaa archive -d {{pad/naar/map}} -o {{pad/naar/uitvoer_bestand.yaa}}`

- Maak een archief van een bestand:

`yaa archive -i {{pad/naar/bestand}} -o {{pad/naar/uitvoer_bestand.yaa}}`

- Pak een archief uit naar de huidige map:

`yaa extract -i {{pad/naar/archive_file.yaa}}`

- Lijst de inhoud van een archief op:

`yaa list -i {{pad/naar/archive_file.yaa}}`

- Maak een archief met een specifiek compressie-algoritme:

`yaa archive -a {{algoritme}} -d {{pad/naar/map}} -o {{pad/naar/uitvoer_bestand.yaa}}`

- Maak een archief met een blokgrootte van 8 MB:

`yaa archive -b 8m -d {{pad/naar/map}} -o {{pad/naar/uitvoer_bestand.yaa}}`
