# ect

> Efficiente Tool di Compressione (o ECT) è un ottimizzatore di file scritto in C++. Supporta file PNG, JPEG, GZIP e ZIP.
> Maggiori informazioni: <https://github.com/fhanau/Efficient-Compression-Tool>.

- Comprimi un file:

`ect {{file.png}}`

- Comprimi un file con il massimo livello di compressione utilizzanto più thread:

`ect -9 --mt-deflate {{file.png}}`

- Comprimi tutti i file in una directory ricorsivamente, mantenendo la data di modifica originale:

`ect -keep -recurse {{percorso/della/directory}}`
