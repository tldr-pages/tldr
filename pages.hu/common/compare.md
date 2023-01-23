# compare

> 2 kép közötti különbség megtekintése. További információ: <https://imagemagick.org/script/compare.php>.

- 2 kép összehasonlítása:

`compare {{image1.png}} {{image2.png}} {{diff.png}}`

- 2 kép összehasonlítása egy egyéni mérőszám segítségével:

`compare -verbose -metric {{PSNR}} {{image1.png}} {{image2.png}} {{diff.png}}`
