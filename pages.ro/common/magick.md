# magick

> Creați, editați, compuneți sau convertiți imagini bitmap.
> ImageMagick versiunea 7+. A se vedea `convert` pentru versiunile 6 și mai jos.
> Mai multe informaţii: <https://imagemagick.org/>

- Conversia tipului de fișier:

`magick {{image.png}} {{image.jpg}}`

- Redimensionați o imagine, făcând o copie nouă:

`magick convert -resize {{100x100}} {{image.jpg}} {{image.jpg}}`

- Creați un GIF folosind imagini:

`magick {{*.jpg}} {{images.gif}}`

- Creați model de tablă de șah:

`magick -size {{640x480}} pattern:checkerboard {{checkerboard.png}}`

- Conversia imaginilor în pagini PDF individuale:

`magick {{*.jpg}} +adjoin {{page-%d.pdf}}`
