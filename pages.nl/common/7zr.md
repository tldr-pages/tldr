# 7zr

> Bestandsarchiver met een hoge compressieverhouding.
> Vergelijkbaar met `7z`, behalve dat het alleen 7z-bestanden ondersteunt.
> Meer informatie: <https://manned.org/7zr>.

- Archiveer een bestand of map:

`7zr a {{pad/naar/archief.7z}} {{pad/naar/bestand_of_map}}`

- Versleutel een bestaand archief (inclusief bestandsnamen):

`7zr a {{pad/naar/versleuteld.7z}} -p{{wachtwoord}} -mhe={{on}} {{pad/naar/archief.7z}}`

- Pak een archief uit met behoud van de originele map structuur:

`7zr x {{pad/naar/archief.7z}}`

- Pak een archief uit naar een specifieke map:

`7zr x {{pad/naar/archief.7z}} -o{{pad/naar/uitkomst}}`

- Pak een archief uit naar `stdout`:

`7zr x {{pad/naar/archief.7z}} -so`

- Geef een [l]ijst met de inhoud van het archiefbestand:

`7zr l {{pad/naar/archief.7z}}`

- Zet het niveau van compressie (hoger betekent meer compressie, maar langzamer):

`7zr a {{pad/naar/archief.7z}} -mx={{0|1|3|5|7|9}} {{pad/naar/bestand_of_map}}`
