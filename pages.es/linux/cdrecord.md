# cdrecord

> Graba datos en CD o DVD.
> Algunas opciones de cdrecord pueden provocar acciones destructivas, como borrar todos los datos de un disco.
> Más información: <https://manned.org/cdrecord>.

- Muestra las unidades ópticas disponibles para `cdrecord`:

`cdrecord --devices`

- Graba un disco solamente de audio:

`cdrecord dev={{/dev/optical_drive}} -audio {{track*.cdaudio}}`

- Graba un archivo en un disco y lo expulsa una vez finalizado (algunas grabadoras lo requieren):

`cdrecord -eject dev={{/dev/optical_drive}} -data {{archivo.iso}}`

- Graba un archivo en el disco de una unidad óptica, con la posibilidad de escribir en varios discos sucesivamente:

`cdrecord -tao dev={{/dev/optical_drive}} -data {{archivo.iso}}`
