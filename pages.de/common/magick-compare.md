# magick compare

> Zeige Unterschiede von zwei Bildern.
> Weitere Informationen: <https://imagemagick.org/script/compare.php>.

- Vergleiche 2 Bilder:

`magick compare {{pfad/zu/bild1.png}} {{pfad/zu/bild2.png}} {{pfad/zu/diff.png}}`

- Vergleiche 2 Bilder mit einer bestimmten Metrik (standardmäßig NCC):

`magick compare -verbose -metric {{PSNR}} {{pfad/zu/bild1.png}} {{pfad/zu/bild2.png}} {{pfad/zu/diff.png}}`
