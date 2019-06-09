# convert

> Strumento della suite immagineMagick per la conversione di immagini.
> Maggiori informazioni: <https://imagemagick.org/script/convert.php>.

- Converti un'immagine da JPG a PNG:

`convert {{immagine.jpg}} {{immagine.png}}`

- Scala un'immagine al 50% delle sue dimensioni originali:

`convert {{immagine.png}} -resize 50% {{immagine2.png}}`

- Scala un'immagine ad una dimensione massima di 640x480 mantenendo le proporzioni originali:

`convert {{immagine.png}} -resize 640x480 {{immagine2.png}}`

- Concatena più immagini orizzontalmente:

`convert {{immagine1.png}} {{immagine2.png}} {{immagine3.png}} +append {{immagine123.png}}`

- Crea una GIF da una serie di immagini con un intervallo di 100ms tra ogni immagine:

`convert {{immagine1.png}} {{immagine2.png}} {{immagine3.png}} -delay {{100}} {{animazione.gif}}`

- Crea un'immagine a tinta unita di un determinato colore:

`convert -size {{800x600}} "xc:{{#ff0000}}" {{immagine.png}}`
