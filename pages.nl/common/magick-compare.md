# magick compare

> Maak een vergelijkingsafbeelding om visueel de verschillen te zien tussen twee afbeeldingen.
> Bekijk ook: `magick`.
> Meer informatie: <https://imagemagick.org/script/compare.php>.

- Vergelijk twee afbeeldingen:

`magick compare {{pad/naar/afbeelding1.png}} {{pad/naar/afbeelding2.png}} {{pad/naar/diff.png}}`

- Vergelijk twee afbeelding door gebruik te maken van de gespecificeerde metriek:

`magick compare -verbose -metric {{PSNR}} {{pad/naar/afbeelding1.png}} {{pad/naar/afbeelding2.png}} {{pad/naar/diff.png}}`
