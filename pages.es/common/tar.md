# tar

> Utilidad de archivado.
> A menudo se combina con un método de compresión, como gzip o bzip2.
> Más información: <https://www.gnu.org/software/tar>.

- [c]rea un archivo y lo escribe en un [f]ile:

`tar cf {{ruta/a/objetivo.tar}} {{ruta/a/archivo1 ruta/a/archivo2 ...}}`

- c]rea un archivo g[z]ipado y lo escribe en un [f]ile:

`tar czf {{ruta/a/objetivo.tar.gz}} {{ruta/a/archivo1 ruta/a/archivo2 ...}}`

- c]rea un archivo g[z]ipado desde un directorio utilizando rutas relativas:

`tar czf {{ruta/a/objetivo.tar.gz}} --directory={{ruta/a/directorio}} .`

- E[x]trae un [f]ile (comprimido) al directorio actual [v]erbosamente:

`tar xvf {{ruta/a/fuente.tar[.gz|.bz2|.xz]}}`

- E[x]trae un [f]ile (comprimido) al directorio de destino:

`tar xf {{ruta/a/fuente.tar[.gz|.bz2|.xz]}}} --directory={{ruta/a/directorio}}`

- Crea un archivo comprimido y lo escribe en una carpeta, utilizando la extensión del archivo para determinar automáticamente el programa de compresión:

`tar caf {{ruta/a/objetivo.tar.xz}} {{ruta/a/archivo1 ruta/a/archivo2 ...}}`

- Lis[t]a el contenido de un [f]ile tar [v]erbosamente:

`tar tvf {{ruta/a/fuente.tar}}`

- E[x]trae ficheros que coincidan con un patrón de un [f]ile:

`tar xf {{ruta/fuente.tar}} --wildcards "{{*.html}}"`
