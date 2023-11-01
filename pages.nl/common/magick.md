# magick

> Creër, bewerk, vorm, of converteer bitmapafbeeldingen.
> ImageMagick versie 7+. Bekijk `convert` voor versies 6 en lager.
> Meer informatie: <https://imagemagick.org/>.

- Converteer bestandstype:

`magick {{pad/naar/invoer_afbeelding.png}} {{pad/naar/uitvoer_afbeelding.jpg}}`

- Formaat van een afbeelding wijzigen, maak een nieuw kopie:

`magick {{pad/naar/invoer_afbeelding.png}} -resize {{100x100}} {{pad/naar/uitvoer_afbeelding.jpg}}`

- Creër een GIF door middel van afbeeldingen:

`magick {{*.jpg}} {{pad/naar/uitvoer_afbeelding.gif}}`

- Creër een dambordpatroon:

`magick -size {{640x480}} pattern:checkerboard {{pad/naar/dambordpatroon.png}}`

- Converteer afbeeldingen naar individuele PDF-pagina's:

`magick {{*.jpg}} -adjoin {{pad/naar/pagina-%d.pdf}}`
