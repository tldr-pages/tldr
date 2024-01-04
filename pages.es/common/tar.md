# tar

> Utilidad de archivado.
> A menudo se combina con un método de compresión, como gzip o bzip2.
> Más información: <https://www.gnu.org/software/tar>.

- [c]rea un archivo y lo escribe en un [f]ile:

`tar cf {{ruta/al/objetivo.tar}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- [c]rea un archivo g[z]ipado y lo escribe en un [f]ile:

`tar czf {{ruta/al/objetivo.tar.gz}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- [c]rea un archivo g[z]ipado desde un directorio utilizando rutas relativas:

`tar czf {{ruta/al/objetivo.tar.gz}} --directory={{ruta/al/directorio}} .`

- E[x]trae un [f]ile (comprimido) al directorio actual [v]erbosamente:

`tar xvf {{ruta/a/fuente.tar[.gz|.bz2|.xz]}}`

- E[x]trae un [f]ile (comprimido) al directorio de destino:

`tar xf {{ruta/al/fuente.tar[.gz|.bz2|.xz]}} --directory={{ruta/al/directorio}}`

- Crea un archivo comprimido y lo escribe en una carpeta, utilizando la extensión del archivo para determinar automáticamente el programa de compresión:

`tar caf {{ruta/al/objetivo.tar.xz}} {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Lis[t]a el contenido de un [f]ile tar [v]erbosamente:

`tar tvf {{ruta/al/fuente.tar}}`

- E[x]trae ficheros que coincidan con un patrón de un [f]ile:

`tar xf {{ruta/al/fuente.tar}} --wildcards "{{*.html}}"`
