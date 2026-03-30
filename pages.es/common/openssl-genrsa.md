# openssl genrsa

> Genera claves privadas RSA.
> Más información: <https://docs.openssl.org/master/man1/openssl-genrsa/>.

- Genera una clave privada RSA de 2048 bits en `stdout`:

`openssl genrsa`

- Guarda una clave privada RSA de un número arbitrario de bits en el archivo de salida:

`openssl genrsa -out {{archivo_salida.key}} {{1234}}`

- Genera una clave privada RSA y la cifra con AES256 (se pedirá una frase de contraseña):

`openssl genrsa {{-aes256}}`
