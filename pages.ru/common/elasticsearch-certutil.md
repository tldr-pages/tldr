# elasticsearch-certutil

> Генерировать SSL-сертификаты для безопасности Elasticsearch и управлять ими.
> Больше информации: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/certutil>.

- Сгенерировать новый центр сертификации (CA) с параметрами по умолчанию:

`elasticsearch-certutil ca`

- Сгенерировать новый сертификат с использованием встроенного CA:

`elasticsearch-certutil cert`

- Сгенерировать сертификаты в неинтерактивном режиме и вывести файлы PEM:

`elasticsearch-certutil cert {{[-s|--silent]}} --pem`

- Сгенерировать HTTP-сертификаты с использованием встроенного CA:

`elasticsearch-certutil http`

- Сгенерировать транспортные сертификаты в неинтерактивном режиме:

`elasticsearch-certutil transport {{[-s|--silent]}}`

- Сгенерировать запрос на подпись сертификата (CSR):

`elasticsearch-certutil csr`

- Сгенерировать зашифрованные пароли хранилища ключей:

`elasticsearch-certutil password`

- Сгенерировать пароль хранилища ключей с указанным значением:

`elasticsearch-certutil password --pass {{пароль}}`
