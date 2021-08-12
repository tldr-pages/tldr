# convert

> Instrumentul de conversie a imaginilor ImageMagick.
> Mai multe informaţii: <https://imagemagick.org/script/convert.php>

- Conversia unei imagini de la JPG la PNG:

`convert {{image.jpg}} {{image.png}}`

- Scala o imagine 50% dimensiunea sa originală:

`convert {{image.png}} -resize 50% {{image2.png}}`

- Scalaţi o imagine păstrând raportul de aspect original la o dimensiune maximă de 640x480:

`convert {{image.png}} -resize 640x480 {{image2.png}}`

- Adaugă orizontal imagini:

`convert {{image1.png}} {{image2.png}} {{image3.png}} +append {{image123.png}}`

- Adaugă vertical imagini:

`convert {{image1.png}} {{image2.png}} {{image3.png}} -append {{image123.png}}`

- Creați un gif dintr-o serie de imagini cu întârziere de 100ms între ele:

`convert {{image1.png}} {{image2.png}} {{image3.png}} -delay {{10}} {{animation.gif}}`

- Creați o imagine cu nimic altceva decât un fundal solid:

`convert -size {{800x600}} "xc:{{#ff0000}}" {{image.png}}`

- Creați un favicon din mai multe imagini de diferite dimensiuni:

`convert {{image1.png}} {{image2.png}} {{image3.png}} {{image.ico}}`
