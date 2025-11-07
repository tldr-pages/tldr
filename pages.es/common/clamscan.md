# clamscan

> Un escáner de virus de línea de comandos.
> Más información: <https://docs.clamav.net/manual/Usage/Scanning.html#clamscan>.

- Escanea un archivo buscando vulnerabilidades:

`clamscan {{ruta/al/archivo}}`

- Escanea todos los archivos recursivamente en un directorio específico:

`clamscan -r {{ruta/al/directorio}}`

- Escanea datos desde `stdin`:

`{{comando}} | clamscan -`

- Escanea usando un archivo de bases de datos de virus o directorio de archivos:

`clamscan --database {{ruta/al/archivo_o_directorio_con_base_de_datos}}`

- Escanea el directorio actual y muestra solo los archivos infectados:

`clamscan --infected`

- Imprime el informe de la exploración a un archivo de registro (log):

`clamscan --log {{ruta/al/archivo_de_registro}}`

- Mueve archivos infectados a un directorio específico:

`clamscan --move {{ruta/al/directorio_de_cuarentena}}`

- Elimina los archivos infectados:

`clamscan --remove yes`
