# openssl genpkey

> Генерировать асимметричные пары ключей.
> Больше информации: <https://docs.openssl.org/master/man1/openssl-genpkey/>.

- Сгенерировать приватный ключ RSA длиной 2048 бит, сохранив его в указанный файл:

`openssl genpkey -algorithm rsa -pkeyopt rsa_keygen_bits:{{2048}} -out {{путь/к/приватному_ключу.key}}`

- Сгенерировать приватный ключ на эллиптической кривой `prime256v1`, сохранив его в указанный файл:

`openssl genpkey -algorithm EC -pkeyopt ec_paramgen_curve:{{prime256v1}} -out {{путь/к/приватному_ключу.key}}`

- Сгенерировать приватный ключ на эллиптической кривой `ED25519`, сохранив его в указанный файл:

`openssl genpkey -algorithm {{ED25519}} -out {{путь/к/приватному_ключу.key}}`
