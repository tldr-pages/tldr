# ibmcloud login

> Входить в IBM Cloud.
> Больше информации: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_login>.

- Войти в интерактивном режиме:

`ibmcloud login`

- Войти, указав конкретную конечную точку API (по умолчанию `cloud.ibm.com`):

`ibmcloud login -a {{конечная_точка_api}}`

- Войти, указав имя пользователя, пароль и целевой регион в качестве параметров:

`ibmcloud login -u {{имя_пользователя}} -p {{пароль}} -r {{us-south}}`

- Войти с использованием API-ключа, передав его как аргумент:

`ibmcloud login --apikey {{строка_api_ключа}}`

- Войти с использованием API-ключа, передав его как файл:

`ibmcloud login --apikey @{{путь/к/файлу_api_ключа}}`

- Войти с использованием федеративного идентификатора (единый вход):

`ibmcloud login --sso`
