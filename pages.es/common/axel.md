# axel

> Acelerador de descargas.
> Protocolos soportados HTTP, HTTPS y FTP.
> Vea también: `aria2c`.
> Más información: <https://manned.org/axel>.

- Descarga un archivo alojado en una URL:

`axel {{url}}`

- Descarga y especifica un nombre de archivo:

`axel {{url}} {{[-o|--output]}} {{ruta/al/archivo}}`

- Descarga con múltiples conexiones:

`axel {{[-n|--num-connections]}} {{num_conexiones}} {{url}}`

- Busca copias espejo:

`axel {{[-S|--search=]}}{{number}} {{num_de_espejos}} {{url}}`

- Limita la velocidad de descarga (bytes por segundo):

`axel {{[-s|--max-speed]}} {{velocidad}} {{url}}`
