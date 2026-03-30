# openssl rand

> Genera bytes aleatorios usando un PRNG criptográficamente seguro.
> Más información: <https://docs.openssl.org/master/man1/openssl-rand/>.

- Genera una cadena hexadecimal de 8 bytes (16 caracteres) y la escribe en `stdout`:

`openssl rand -hex 8`

- Genera 20 bytes aleatorios codificados en base64:

`openssl rand -base64 20`

- Genera bytes aleatorios y los escribe en un archivo (sin codificación):

`openssl rand -out {{ruta/al/archivo}} {{longitud}}`

- Genera 1 KiB/MiB/GiB/TiB de bytes aleatorios codificados en hex/base64:

`openssl rand -{{hex|base64}} 1{{K|M|G|T}}`
