# convert

> Imagemagick Bildkonvertierungswerkzeug
> Mehr Informationen: <https://imagemagick.org/script/convert.php>

- Konvertiere ein Bild von JPG nach PNG:

`convert {{image.jpg}} {{image.png}}`

- Ein Bild auf 50% seiner Originalgröße skalieren:

`convert {{image.png}} -resize 50% {{image2.png}}`

- Skaliere ein Bild unter Beibehaltung des ursprünglichen Seitenverhältnisses auf eine maximale Größe von 640x480:

`convert {{image.png}} -resize 640x480 {{image2.png}}`

- Bilder horizontal aneinader hängen:

`convert {{image1.png}} {{image2.png}} {{image3.png}} +append {{image123.png}}`

- Bilder vertikal aneinander hängen:

`convert {{image1.png}} {{image2.png}} {{image3.png}} -append {{image123.png}}`

- Erstellen Sie ein Gif aus einer Serie von Bildern mit einer Verzögerung von 100 ms zwischen den Bildern:

`convert {{image1.png}} {{image2.png}} {{image3.png}} -delay {{10}} {{animation.gif}}`

- Erstellen Sie ein Bild mit nichts als einem festen Hintergrund:

`convert -size {{800x600}} "xc:{{#ff0000}}" {{image.png}}`
