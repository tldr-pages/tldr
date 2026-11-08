# ibmcloud config

> Изменять или просматривать значения конфигурации CLI IBM Cloud.
> Больше информации: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_config>.

- Установить тайм-аут HTTP-запросов на 30 секунд:

`ibmcloud config --http-timeout 30`

- Включить трассировку HTTP-запросов:

`ibmcloud config --trace true`

- Перенаправить трассировку HTTP-запросов в конкретный файл:

`ibmcloud config --trace {{путь/к/файлу_трассировки}}`

- Отключить цветной вывод:

`ibmcloud config --color false`

- Установить локаль на конкретный язык:

`ibmcloud config --locale {{zh_Hans}}`

- Включить автоматическое принятие одноразового кода SSO:

`ibmcloud config --sso-otp auto`
