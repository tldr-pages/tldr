# yaa

> Maak en beheer YAA-archieven.
> Meer informatie: <https://www.manpagez.com/man/1/yaa/>.

- Maak een archief van een map:

`yaa archive -d {{pad/naar/map}} -o {{pad/naar/uitvoer_bestand.yaa}}`

- Maak een archief van een bestand:

`yaa archive -i {{pad/naar/bestand}} -o {{pad/naar/uitvoer_bestand.yaa}}`

- Pak een archief uit naar de huidige map:

`yaa extract -i {{pad/naar/archive_file.yaa}}`

- Toon de inhoud van een archief:

`yaa list -i {{pad/naar/archive_file.yaa}}`

- Maak een archief met een specifiek compressie-algoritme:

`yaa archive -a {{algoritme}} -d {{pad/naar/map}} -o {{pad/naar/uitvoer_bestand.yaa}}`

- Maak een archief met een blokgrootte van 8 MB:

`yaa archive -b 8m -d {{pad/naar/map}} -o {{pad/naar/uitvoer_bestand.yaa}}`
