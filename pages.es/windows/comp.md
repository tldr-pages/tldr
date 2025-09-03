# comp

> Compara el contenido de dos archivos o conjunto de archivos.
> Usa comodines (*) para comparar conjuntos de archivos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/comp>.

- Compara archivos de forma interactiva:

`comp`

- Comparar dos archivos especificos:

`comp {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Comparar dos conjuntos de archivos:

`comp {{ruta\al\directorio1}}\* {{ruta\al\directorio2}}\*`

- Mostrar las diferencias en formato [d]ecimal:

`comp /d {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Mostrar las diferencias en formato [a]SCII:

`comp /a {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Mostrar los números de [l]ínea para las diferencias:

`comp /l {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Comparar archivos sin diferenciar mayúsculas y minúsculas ([c]ase-insensitive):

`comp /c {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- CComparar solo las primeras 5 líneas de cada archivo:

`comp /n=5 {{ruta\al\archivo1}} {{ruta\al\archivo2}}`
