# openssl genrsa

> Генерировать приватные ключи RSA.
> Больше информации: <https://docs.openssl.org/master/man1/openssl-genrsa/>.

- Сгенерировать приватный ключ RSA длиной 2048 бит в `stdout`:

`openssl genrsa`

- Сохранить приватный ключ RSA произвольной длины в выходной файл:

`openssl genrsa -out {{выходной_файл.key}} {{1234}}`

- Сгенерировать приватный ключ RSA и зашифровать его с помощью AES256 (будет запрошена парольная фраза):

`openssl genrsa {{-aes256}}`
