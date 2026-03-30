# openssl

> Kit de herramientas criptográficas OpenSSL.
> Algunos subcomandos como `req` tienen su propia documentación de uso.
> Más información: <https://docs.openssl.org/master/man1/openssl/>.

- Genera una clave privada y cifra el archivo de salida usando AES-256:

`openssl genpkey -algorithm {{rsa|ec}} -out {{ruta/a/privada.key}} -aes256`

- Genera la clave pública correspondiente a partir de la clave privada usando `rsa`:

`openssl rsa -in {{ruta/a/privada.key}} -pubout -out {{ruta/a/publica.key}}`

- Genera un certificado autofirmado válido por un número específico de días (365):

`openssl req -new -x509 -key {{ruta/a/privada.key}} -out {{ruta/a/certificado.crt}} -days 365`

- Convierte un certificado al formato `.pem` o `.der`:

`openssl x509 -in {{ruta/a/certificado.crt}} -out {{ruta/a/certificado.pem|ruta/a/certificado.der}} -outform {{pem|der}}`

- Verifica los detalles de un certificado:

`openssl x509 -in {{ruta/a/certificado.crt}} -text -noout`

- Genera una solicitud de firma de certificado (CSR):

`openssl req -new -key {{ruta/a/privada.key}} -out {{ruta/a/solicitud.csr}}`

- Muestra la ayuda:

`openssl help`

- Muestra la versión:

`openssl version`
