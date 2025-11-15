# magick convert

> Outil de conversion d'image d'ImageMagick.
> Plus d'informations : <https://imagemagick.org/script/convert.php>.

- Convertir une image JPEG en PNG :

`magick convert {{image.jpg}} {{image.png}}`

- Redimensionner une image à 50% de ses dimensions d'origine :

`magick convert {{image.png}} -resize 50% {{image2.png}}`

- Redimensionner une image en conservant son ratio hauteur/largeur initial pour une taille maximum de 640x480 :

`magick convert {{image.png}} -resize 640x480 {{image2.png}}`

- Coller plusieurs images horizontallement :

`magick convert {{image1.png}} {{image2.png}} {{image3.png}} +append {{image123.png}}`

- Coller plusieurs images verticalement :

`magick convert {{image1.png}} {{image2.png}} {{image3.png}} -append {{image123.png}}`

- Créer un gif à partir d'une série d'images avec un délai de 100ms entre chaque :

`magick convert {{image1.png}} {{image2.png}} {{image3.png}} -delay {{100}} {{animation.gif}}`

- Créer une image avec un simple arrière-plan uni :

`magick convert -size {{800x600}} "xc:{{#ff0000}}" {{image.png}}`
