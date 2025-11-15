# pamfile

> Describe archivos Netpbm (PAM o PNM).
> Más información: <https://netpbm.sourceforge.net/doc/pamfile.html>.

- Describe los archivos Netpbm especificados:

`pamfile {{ruta/al/archivo1 ruta/al/archivo2 ...}}`

- Describe cada imagen en cada archivo de entrada (a diferencia de la primera imagen en cada archivo) en un formato legible para la máquina:

`pamfile {{[-a|-allimages]}} -machine {{ruta/al/archivo}}`

- Muestra un conteo de cuántas imágenes contiene el archivo:

`pamfile {{[-cou|-count]}} {{ruta/al/archivo}}`
