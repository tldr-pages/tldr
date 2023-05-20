# axel

> Acelerador de descargas.
> Protocolos soportados HTTP, HTTPS y FTP.
> Más información: <https://github.com/axel-download-accelerator/axel>.

- Descarga un archivo alojado en una URL:

`axel {{url}}`

- Descarga y especifica un nombre de archivo:

`axel {{url}} -o {{ruta/al/archivo}}`

- Descarga con múltiples conexiones:

`axel -n {{num_conexiones}} {{url}}`

- Busca un archivo utilizando un mirror haciendo uso del motor de búsqueda filesearching.com.

`axel -S {{num_de_espejos}} {{url}}`

- Limita la velocidad de descarga (bytes por segundo):

`axel -s {{velocidad}} {{url}}`
