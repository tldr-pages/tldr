# axel

> Acelerador de descargas.
> Soporta HTTP, HTTPS y FTP.
> Más información: <https://github.com/axel-download-accelerator/axel>.

- Descarga una URL a un archivo:

`axel {{url}}`

- Descarga y especifica nombre de archivo:

`axel {{url}} -o {{ruta/al/archivo}}`

- Descarga con varias conexiones:

`axel -n {{num_conexiones}} {{url}}`

- Busca copias espejo:

`axel -S {{num_de_espejos}} {{url}}`

- Limita la velocidad de descarga (bytes por segundo):

`axel -s {{velocidad}} {{url}}`
