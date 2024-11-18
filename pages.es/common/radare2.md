# radare2

> Un conjunto de herramientas de ingeniería inversa.
> Más información: <https://www.radare.org/r/docs.html>.

- Abre un archivo en modo escritura sin analizar los encabezados del formato de archivo:

`radare2 -nw {{ruta/al/binario}}`

- Depurar un programa:

`radare2 -d {{ruta/al/binario}}`

- Ejecuta un script antes de entrar en la CLI interactiva:

`radare2 -i {{ruta/a/script.r2}} {{ruta/al/binario}}`

- Muestra texto de ayuda para cualquier comando en el CLI interactivo:

`> {{radare2_command}}?`

- Ejecuta un comando desde el CLI interactivo:

`> !{{shell_command}}`

- Muestra los bytes tal cual del bloque actual a un archivo:

`> pr > {{ruta/al/archivo.bin}}`
