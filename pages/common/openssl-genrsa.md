# openssl genrsa

> OpenSSL command to generate RSA private keys.
> More information: <https://www.openssl.org/docs/man1.0.2/man1/genrsa.html>.

- Generate an RSA private key of 2048 bits to stdout:

`openssl genrsa`

- Save an RSA private key of an arbitrary number of bits to the output file:

`openssl genrsa -out {{output_file.key}} {{1234}}`

- Generate an RSA private key and encrypt it with AES256 (you will be prompted for a passphrase):

`openssl genrsa {{-aes256}}`
