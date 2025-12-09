# fc

> Compara las diferencias entre dos archivos o conjuntos de archivos.
> Usa comodines (*) para comparar conjuntos de archivos.
> Más información: <https://learn.microsoft.com/windows-server/administration/windows-commands/fc>.

- Compara 2 archivos especificados:

`fc {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Realiza una comparación sin distinguir entre mayúsculas y minúsculas:

`fc /c {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Comparar archivos como texto Unicode:

`fc /u {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Comparar archivos como texto ASCII:

`fc /l {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Comparar archivos como binarios:

`fc /b {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Deshabilitar la expansión de tabulaciones a espacios:

`fc /t {{ruta\al\archivo1}} {{ruta\al\archivo2}}`

- Comprimir espacios en blanco (tabulaciones y espacios) para comparaciones:

`fc /w {{ruta\al\archivo1}} {{ruta\al\archivo2}}`
