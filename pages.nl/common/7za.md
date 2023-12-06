# 7za

> Bestandsarchiver met een hoge compressieverhouding.
> Vergelijkbaar met `7z`, behalve dat het minder bestandstypes ondersteunt, maar platformonafhankelijk is.
> Meer informatie: <https://manned.org/7za>.

- Archiveer een bestand of map:

`7za a {{pad/naar/archief.7z}} {{pad/naar/bestand_of_map}}`

- Versleutel een bestaand archief (inclusief bestandsnamen):

`7za a {{pad/naar/versleuteld.7z}} -p{{wachtwoord}} -mhe={{on}} {{pad/naar/archief.7z}}`

- Pak een archief uit met behoud van de originele map structuur:

`7za x {{pad/naar/archief.7z}}`

- Pak een archief uit naar een specifieke map:

`7za x {{pad/naar/archief.7z}} -o{{pad/naar/uitkomst}}`

- Pak een archief uit naar `stdout`:

`7za x {{pad/naar/archief.7z}} -so`

- Archiveren met een specifiek archieftype:

`7za a -t{{7z|bzip2|gzip|lzip|tar|...}} {{pad/naar/archief.7z}} {{pad/naar/bestand_of_map}}`

- Geef een [l]ijst met de inhoud van het archiefbestand:

`7za l {{pad/naar/archief.7z}}`

- Zet het niveau van compressie (hoger betekent meer compressie, maar langzamer):

`7za a {{pad/naar/archief.7z}} -mx={{0|1|3|5|7|9}} {{pad/naar/bestand_of_map}}`
