# magick montage

> Plaats afbeeldingen in een aanpasbaar raster.
> Bekijk ook: `magick`.
> Meer informatie: <https://imagemagick.org/script/montage.php>.

- Plaats afbeeldingen in een raster, waarbij afbeeldingen die groter zijn dan de rastercelgrootte automatisch worden aangepast:

`magick montage {{pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...}} {{pad/naar/montage.jpg}}`

- Plaats afbeeldingen in een raster, waarbij de rastercelgrootte automatisch wordt berekend op basis van de grootste afbeelding:

`magick montage {{pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...}} -geometry {{+0+0}} {{pad/naar/montage.jpg}}`

- Specificeer de rastercelgrootte en pas de afbeeldingen aan om hierin te passen voordat ze worden geplaatst:

`magick montage {{pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...}} -geometry {{640x480+0+0}} {{pad/naar/montage.jpg}}`

- Beperk het aantal rijen en kolommen in het raster, waardoor invoerafbeeldingen over meerdere output-montages worden verdeeld:

`magick montage {{pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...}} -geometry {{+0+0}} -tile {{2x3}} {{montage_%d.jpg}}`

- Wijzig de grootte en snijd afbeeldingen bij om hun rastercellen te vullen voordat ze worden geplaatst:

`magick montage {{pad/naar/afbeelding1.jpg pad/naar/afbeelding2.jpg ...}} -geometry {{+0+0}} -resize {{640x480^}} -gravity {{center}} -crop {{640x480+0+0}} {{pad/naar/montage.jpg}}`
