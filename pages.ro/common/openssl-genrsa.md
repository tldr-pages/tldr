# openssl genrsa

> comanda OpenSSL pentru a genera chei private RSA.
> Mai multe informaţii: <https://www.openssl.org/docs/manmaster/man1/openssl-genrsa.html>

- Generați o cheie privată RSA de 2048 biți pentru a stdout:

`openssl genrsa`

- Salvați o cheie privată RSA a unui număr arbitrar de biți în fișierul de ieșire:

`openssl genrsa -out {{output_file.key}} {{1234}}`

- Generați o cheie privată RSA și criptați-o cu AES256 (vi se va solicita o frază de acces):

`openssl genrsa {{-aes256}}`
