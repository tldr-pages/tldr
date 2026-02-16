# openssl

> Криптографический набор инструментов OpenSSL.
> Некоторые подкоманды, такие как `req`, имеют собственную документацию.
> Больше информации: <https://docs.openssl.org/master/man1/openssl/>.

- Сгенерировать закрытый ключ и зашифровать выходной файл с помощью AES256:

`openssl genpkey -algorithm {{rsa|ec}} -out {{private.key}} -aes256`

- Сгенерировать соответствующий открытый ключ из закрытого ключа `private.key` с помощью `rsa`:

`openssl rsa -in {{private.key}} -pubout -out {{public.key}}`

- Сгенерировать самоподписанный сертификат, действительный указанное количество дней (`365`):

`openssl req -new -x509 -key {{private.key}} -out {{certificate.crt}} -days {{365}}`

- Конвертировать сертификат в формат `pem` или `der`:

`openssl x509 -in {{certificate.crt}} -out {{certificate.pem|certificate.der}} -outform {{pem|der}}`

- Просмотреть детали сертификата:

`openssl x509 -in {{certificate.crt}} -text -noout`

- Сгенерировать запрос на подпись сертификата (CSR):

`openssl req -new -key {{private.key}} -out {{request.csr}}`

- Показать справку:

`openssl help`

- Показать версию:

`openssl version`
