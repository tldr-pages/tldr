# magick identify

> Beschrijf het formaat en eigenschappen van afbeeldingen.
> Bekijk ook: `magick`.
> Meer informatie: <https://imagemagick.org/script/identify.php>.

- Beschrijf het formaat en basis eigenschappen van een afbeelding:

`magick identify {{pad/naar/afbeelding}}`

- Beschrijf het formaat en uitgebreide eigenschappen van een afbeelding:

`magick identify -verbose {{pad/naar/afbeelding}}`

- Verzamel de dimensies van alle JPEG bestanden in de huidige map en sla ze op naar een CSV-bestand:

`magick identify -format "{{%f,%w,%h\n}}" {{*.jpg}} > {{pad/naar/bestandslijst.csv}}`
