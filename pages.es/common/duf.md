# duf

> Utilidad de uso/espacio libre de disco.
> Vea también: `ncdu`, `df`.
> Más información: <https://github.com/muesli/duf#usage>.

- Lista los dispositivos accesibles:

`duf`

- Lista todo (como sistemas de archivos pseudo, duplicados o inaccesibles):

`duf --all`

- Muestra solo los dispositivos o puntos de montaje especificados:

`duf {{ruta/al/directorio1 ruta/al/directorio2 ...}}`

- Ordena la salida según un criterio específico:

`duf --sort {{size|used|avail|usage}}`

- Muestra u oculta sistemas de archivos específicos:

`duf --{{only-fs|hide-fs}} {{tmpfs|vfat|ext4|xfs}}`

- Ordena la salida por clave:

`duf --sort {{mountpoint|size|used|avail|usage|inodes|inodes_used|inodes_avail|inodes_usage|type|filesystem}}`

- Cambia el tema (si `duf` no consigue usar el tema correcto):

`duf --theme {{dark|light}}`
