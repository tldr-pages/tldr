# openssl s_client

> Создавать клиентские TLS-соединения.
> Больше информации: <https://docs.openssl.org/master/man1/openssl-s_client/>.

- Показать даты начала и окончания действия сертификата домена:

`openssl s_client -connect {{хост}}:{{порт}} 2>/dev/null | openssl x509 -noout -dates`

- Показать сертификат, предоставленный SSL/TLS-сервером:

`openssl < /dev/null s_client -connect {{хост}}:{{порт}}`

- Указать индикатор имени сервера (SNI) при подключении к SSL/TLS-серверу:

`openssl s_client -connect {{хост}}:{{порт}} -servername {{имя_хоста}}`

- Показать полную цепочку сертификатов HTTPS-сервера:

`openssl < /dev/null s_client -connect {{хост}}:443 -showcerts`
