# openssl genrsa

> OpenSSL parancs az RSA magánkulcsok generálásához. További információ: <https://www.openssl.org/docs/manmaster/man1/openssl-genrsa.html>.

- Generáljon egy 2048 bites RSA magánkulcsot a `stdout` címen:

`openssl genrsa`

- Tetszőleges számú bitből álló RSA magánkulcs mentése a kimeneti fájlba:

`openssl genrsa -out {{output_file.key}} {{1234}}`

- Generáljon egy RSA magánkulcsot, és titkosítja azt AES256-tal (a program kérni fogja a jelszót):

`openssl genrsa {{-aes256}}`
