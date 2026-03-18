# zip

> Empaqueta y comprime (archiva) archivos en un archivo Zip.
> Vea también: `unzip`.
> Más información: <https://manned.org/zip>.

- Añade archivos/directorios a un archivo específico:

`zip {{[-r|--recurse-paths]}} {{ruta/a/archivo_comprimido.zip}} {{ruta/a/archivo_o_directorio1 ruta/a/archivo_o_directorio2 ...}}`

- Elimina archivos/directorios de un archivo específico:

`zip {{[-d|--delete]}} {{ruta/a/archivo_comprimido.zip}} {{ruta/a/archivo_o_directorio1 ruta/a/archivo_o_directorio2 ...}}`

- Archiva archivos/directorios excluyendo los especificados:

`zip {{[-r|--recurse-paths]}} {{ruta/a/archivo_comprimido.zip}} {{ruta/a/archivo_o_directorio1 ruta/a/archivo_o_directorio2 ...}} {{[-x|--exclude]}} {{ruta/a/archivos_o_directorios_excluidos}}`

- Archiva archivos/directorios con un nivel de compresión específico (`0` - el más bajo, `9` - el más alto):

`zip {{[-r|--recurse-paths]}} -{{0..9}} {{ruta/a/archivo_comprimido.zip}} {{ruta/a/archivo_o_directorio1 ruta/a/archivo_o_directorio2 ...}}`

- Crea un archivo cifrado con una contraseña específica:

`zip {{[-re|--recurse-paths --encrypt]}} {{ruta/a/archivo_comprimido.zip}} {{ruta/a/archivo_o_directorio1 ruta/a/archivo_o_directorio2 ...}}`

- Archiva archivos/directorios en un archivo Zip dividido en varias partes (por ejemplo, partes de 3 GB):

`zip {{[-rs|--recurse-paths --split-size]}} {{3g}} {{ruta/a/archivo_comprimido.zip}} {{ruta/a/archivo_o_directorio1 ruta/a/archivo_o_directorio2 ...}}`

- Imprime el contenido de un archivo específico:

`zip {{[-sf|--split-size --freshen]}} {{ruta/a/archivo_comprimido.zip}}`
