# magick

> Creër, bewerk, vorm, of converteer bitmapafbeeldingen.
> ImageMagick versie 7+. Bekijk `convert` versies 6 en lager.
> Meer informatie: <https://imagemagick.org/>.

- Converteer bestandstype:

`magick {{afbeelding.png}} {{afbeelding.jpg}}`

- Formaat van een afbeelding wijzigen, maak een nieuw kopie:

`magick convert -resize {{100x100}} {{afbeelding.jpg}} {{afbeelding.jpg}}`

- Creër een GIF door middel van afbeeldingen:

`magick {{*.jpg}} {{afbeelding.gif}}`

- Creër een dambordpatroon:

`magick -size {{640x480}} pattern:checkerboard {{dambordpatroon.png}}`

- Converteer afbeeldingen naar individuele PDF-pagina's:

`magick {{*.jpg}} +adjoin {{pagina-%d.pdf}}`
