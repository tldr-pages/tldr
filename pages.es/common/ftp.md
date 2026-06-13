# ftp

> Herramientas para interactuar con un servidor a través del Protocolo de Transferencia de Archivos.
> Más información: <https://manned.org/ftp>.

- Se conecta a un servidor FTP:

`ftp {{ftp.example.com}}`

- Se conecta a un servidor FTP especificando su dirección IP y su puerto:

`ftp {{dirección_ip}} {{puerto}}`

- Cambia al modo de transferencia binario (gráficos, archivos comprimidos, etc):

`binary`

- Transfiere varios archivos sin pedir confirmación por cada archivo:

`prompt off`

- Descarga varios archivos (expresión glob):

`mget {{*.png}}`

- Carga varios archivos (expresión glob):

`mput {{*.zip}}`

- Elimina varios archivos del servidor remoto:

`mdelete {{*.txt}}`

- Cambia el nombre de un archivo en el servidor remoto:

`rename {{nombre_archivo_original}} {{nuevo_nombre_archivo}}`
