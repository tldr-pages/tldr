# fdisk

> Gestiona tablas de particiones y particiones en una unidad de almacenamiento.
> Vea también: `partprobe`, `parted`, `cfdisk`.
> Más información: <https://manned.org/fdisk>.

- Lista las particiones:

`sudo fdisk {{[-l|--list]}}`

- Inicia el manipulador interactivo de particiones:

`sudo fdisk {{/dev/sdX}}`

- Abre un [m]enú de ayuda:

`<m>`

- Muestra la tabla de [p]articiones:

`<p>`

- Crea una [n]ueva partición:

`<n>`

- Selecciona una partición para eliminar [d]:

`<d>`

- Escribe [w] los cambios realizados:

`<w>`

- Descarta los cambios realizados y sale [q]:

`<q>`
