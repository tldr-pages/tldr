# elasticsearch-keystore

> Управлять защищёнными настройками (например, паролями, токенами и учётными данными), используемыми в Elasticsearch.
> Больше информации: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/elasticsearch-keystore>.

- Создать новое хранилище ключей (без защиты паролем):

`elasticsearch-keystore create`

- Создать новое хранилище ключей с защитой паролем:

`elasticsearch-keystore create -p`

- Добавить настройку в интерактивном режиме:

`elasticsearch-keystore add {{имя_настройки}}`

- Добавить настройку из `stdin`:

`echo "{{значение_настройки}}" | elasticsearch-keystore add --stdin {{имя_настройки}}`

- Удалить настройку из хранилища ключей:

`elasticsearch-keystore remove {{имя_настройки}}`

- Изменить пароль хранилища ключей:

`elasticsearch-keystore passwd`

- Вывести список всех настроек, сохранённых в хранилище ключей:

`elasticsearch-keystore list`

- Обновить формат хранилища ключей (после обновления Elasticsearch):

`elasticsearch-keystore upgrade`
