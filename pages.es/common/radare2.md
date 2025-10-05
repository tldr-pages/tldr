# radare2

> Un conjunto de herramientas de ingeniería inversa.
> Más información: <https://book.rada.re/first_steps/commandline_flags.html>.

- Abre un archivo en modo escritura sin analizar los encabezados del formato de archivo:

`radare2 -nw {{ruta/al/binario}}`

- Depura un programa:

`radare2 -d {{ruta/al/binario}}`

- Ejecuta un script antes de entrar en la CLI interactiva:

`radare2 -i {{ruta/a/script.r2}} {{ruta/al/binario}}`

- Muestra texto de ayuda para cualquier comando en la CLI interactiva:

`{{radare2_comando}}?`

- Ejecuta un comando desde la CLI interactiva:

`!{{shell_comando}}`

- Vierte los bytes crudos del bloque actual a un archivo:

`> pr > {{ruta/al/archivo.bin}}`
