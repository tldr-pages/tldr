# ibmcloud api

> Устанавливать или просматривать конечную точку API IBM Cloud.
> Больше информации: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_api>.

- Показать текущую конечную точку API:

`ibmcloud api`

- Установить конечную точку API на `cloud.ibm.com`:

`ibmcloud api cloud.ibm.com`

- Установить приватную конечную точку API:

`ibmcloud api private.cloud.ibm.com`

- Использовать VPC-соединение для приватной конечной точки:

`ibmcloud api private.cloud.ibm.com --vpc`

- Пропустить проверку SSL для HTTP-запросов:

`ibmcloud api https://cloud.ibm.com --skip-ssl-validation`

- Удалить настройку конечной точки API:

`ibmcloud api --unset`
