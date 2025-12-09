# qmmp

> Un reproductor de audio con una interfaz similar a Winamp o XMMS.
> Vea también: `clementine`, `ncmpcpp`, `cmus`.
> Más información: <https://manned.org/qmmp>.

- Lanza la interfaz gráfica de usuario (GUI):

`qmmp`

- Comienza o detiene el audio actual:

`qmmp {{[-t|--play-pause]}}`

- Va hacia adelante o hacia atrás una cantidad específica de tiempo en segundos:

`qmmp --seek-{{fwd|bwd}} {{tiempo_en_segundos}}`

- Reproduce el próximo archivo de audio:

`qmmp --next`

- Reproduce el archivo de audio anterior:

`qmmp --previous`

- Muestra el volumen actual:

`qmmp --volume-status`

- [inc]rementa o [dec]rementa el volumen del audio actual en un 5%:

`qmmp --volume-{{inc|dec}}`
