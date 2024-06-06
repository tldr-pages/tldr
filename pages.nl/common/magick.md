# magick

> Creër, bewerk, vorm of converteer bitmapafbeeldingen.
> Deze tool vervangt `convert` in ImageMagick 7+. Bekijk `magick convert` om de oude tool te gebruiken in versies 7+.
> Sommige subcommando's zoals `mogrify` hebben hun eigen documentatie.
> Meer informatie: <https://imagemagick.org>.

- Converteer tussen afbeeldingsformaten:

`magick {{pad/naar/invoer_afbeelding.png}} {{pad/naar/uitvoer_afbeelding.jpg}}`

- Wijzig de grootte van een afbeelding en maak een nieuwe kopie:

`magick {{pad/naar/invoer_afbeelding.png}} -resize {{100x100}} {{pad/naar/uitvoer_afbeelding.jpg}}`

- Maak een GIF van alle JPEG-afbeeldingen uit de huidige map:

`magick {{*.jpg}} {{pad/naar/uitvoer_afbeelding.gif}}`

- Creër een dambordpatroon:

`magick -size {{640x480}} pattern:checkerboard {{pad/naar/dambordpatroon.png}}`

- Maak een PDF van alle JPEG-afbeeldingen uit de huidige map:

`magick {{*.jpg}} -adjoin {{pad/naar/pagina-%d.pdf}}`
