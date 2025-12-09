# clamdscan

> Escaneo de virus con el servicio (daemon) ClamAV.
> Más información: <https://docs.clamav.net/manual/Usage/Scanning.html#clamdscan>.

- Escanea un archivo o directorio buscando vulnerabilidades:

`clamdscan {{ruta/al/archivo_o_directorio}}`

- Escanea desde `stdin`:

`{{comando}} | clamdscan -`

- Escanea el directorio actual y muestra solo los archivos infectados:

`clamdscan --infected`

- Imprime el informe de la exploración a un archivo de registro (log):

`clamdscan --log {{ruta/al/archivo_de_registro}}`

- Mueve los archivos infectados a un directorio específico:

`clamdscan --move {{ruta/a/directorio_de_cuarentena}}`

- Elimina los archivos infectados:

`clamdscan --remove`

- Utiliza varios hilos para escanear un directorio:

`clamdscan --multiscan`

- Pasa el descriptor de archivo en lugar de transmitir el archivo al daemon:

`clamdscan --fdpass`
