# compare

> Zeige Unterschiede von zwei Bildern.
> Mehr Informationen: <https://imagemagick.org/script/compare.php>.

- Vergleiche 2 Bilder:

`compare {{bild1.png}} {{bild2.png}} {{diff.png}}`

- Vergleiche 2 Bilder mit einer bestimmten Metrik:

`compare -verbose -metric {{PSNR}} {{bild1.png}} {{bild2.png}} {{diff.png}}`
