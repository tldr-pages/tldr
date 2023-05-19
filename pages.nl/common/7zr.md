# 7zr

> Bestandsarchiver met een hoge compressieverhouding.
> Vergelijkbaar met `7z`, behalve dat het alleen `.7z`-bestanden ondersteunt.
> Meer informatie: <https://manned.org/7zr>.

- Archiveer een bestand of directory:

`7zr a {{pad/naar/archief.7z}} {{pad/naar/bestand_of_directory}}`

- Versleutel een bestaand archief (inclusief bestandsnamen):

`7zr a {{pad/naar/versleuteld.7z}} -p{{wachtwoord}} -mhe={{on}} {{pad/naar/archief.7z}}`

- Pak een archief uit met behoud van de originele directory structuur:

`7zr x {{pad/naar/archief.7z}}`

- Pak een archief uit naar een specifieke directory:

`7zr x {{pad/naar/archief.7z}} -o{{pad/naar/uitkomst}}`

- Pak een archief uit naar `stdout`:

`7zr x {{pad/naar/archief.7z}} -so`

- Lijst de inhoud van een archief op:

`7zr l {{pad/naar/archief.7z}}`

- Maak een lijst van beschikbare archieftypen:

`7zr i`
