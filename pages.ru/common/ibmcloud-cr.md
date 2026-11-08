# ibmcloud cr

> Управлять содержимым и конфигурацией реестра контейнеров IBM Cloud.
> Больше информации: <https://cloud.ibm.com/docs/cli?topic=cli-containerregcli>.

- Установить целевой регион для реестра контейнеров IBM Cloud:

`ibmcloud cr region-set`

- Показать доступные образы:

`ibmcloud cr {{[images|image-list]}}`

- Просмотреть данные образа:

`ibmcloud cr image-inspect {{образ}}`

- Запустить оценку уязвимостей для образа:

`ibmcloud cr {{[va|vulnerability-assessment]}} {{образ}}`

- Войти в реестр контейнеров IBM Cloud через локальный клиент Docker или Podman:

`ibmcloud cr login`

- Показать все доступные действия для данной команды:

`ibmcloud cr help`
