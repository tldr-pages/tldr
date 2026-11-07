# ibmcloud iam

> Управлять идентификацией и доступом к ресурсам.
> Больше информации: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_commands_iam>.

- Показать идентификаторы сервисов в учётной записи:

`ibmcloud iam service-ids`

- Показать все API-ключи для идентификатора сервиса:

`ibmcloud iam service-api-keys {{идентификатор_сервиса}}`

- Создать API-ключ для идентификатора сервиса с описанием и без подтверждения:

`ibmcloud iam service-api-key-create {{имя_api_ключа}} {{идентификатор_сервиса}} {{[-d|--description]}} {{описание}} {{[-f|--force]}}`

- Показать все доступные действия для данной команды:

`ibmcloud iam help`
