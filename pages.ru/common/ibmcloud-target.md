# ibmcloud target

> Устанавливать или просматривать целевую учётную запись, регион или группу ресурсов.
> Больше информации: <https://cloud.ibm.com/docs/cli?topic=cli-ibmcloud_cli#ibmcloud_target>.

- Показать текущую целевую учётную запись и регион:

`ibmcloud target`

- Установить целевую учётную запись:

`ibmcloud target -c {{идентификатор_учётной_записи}}`

- Переключиться на конкретный регион:

`ibmcloud target -r {{имя_региона}}`

- Установить целевую группу ресурсов:

`ibmcloud target -g {{имя_группы_ресурсов}}`

- Очистить целевой регион:

`ibmcloud target --unset-region`

- Очистить целевую группу ресурсов:

`ibmcloud target --unset-resource-group`
