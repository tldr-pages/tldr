# convert

> ImageMagick képkonvertáló eszköz. További információ: <https://imagemagick.org/script/convert.php>.

- Kép átalakítása JPG-ből PNG-be:

`convert {{image.jpg}} {{image.png}}`

- Egy képet az eredeti méretének 50%-ára méretezhet:

`convert {{image.png}} -resize 50% {{image2.png}}`

- Egy kép méretezése az eredeti képarány megtartásával legfeljebb 640x480-as méretre:

`convert {{image.png}} -resize 640x480 {{image2.png}}`

- Képek vízszintes csatolása:

`convert {{image1.png}} {{image2.png}} {{image3.png}} +append {{image123.png}}`

- Képek függőlegesen történő csatolása:

`convert {{image1.png}} {{image2.png}} {{image3.png}} -append {{image123.png}}`

- GIF létrehozása képsorozatból 100 ms késleltetéssel a képek között:

`convert {{image1.png}} {{image2.png}} {{image3.png}} -delay {{10}} {{animation.gif}}`

- Készítsen egy képet egyszínű háttérrel:

`convert -size {{800x600}} "xc:{{#ff0000}}" {{image.png}}`

- Favicon létrehozása több különböző méretű képből:

`convert {{image1.png}} {{image2.png}} {{image3.png}} {{image.ico}}`
