# elasticsearch-reset-password

> Сбрасывать пароли пользователей нативной области и встроенных пользователей.
> Больше информации: <https://www.elastic.co/docs/reference/elasticsearch/command-line-tools/reset-password>.

- Сбросить пароль пользователя на автоматически сгенерированное значение и вывести его в консоли:

`elasticsearch-reset-password {{[-u|--username]}} {{пользователь}}`

- Сбросить пароль нативного пользователя в интерактивном режиме:

`elasticsearch-reset-password {{[-u|--username]}} {{пользователь}} {{[-i|--interactive]}}`

- Сбросить пароль пользователя в интерактивном режиме на конкретном URL-адресе узла Elasticsearch:

`elasticsearch-reset-password --url {{хост}}:{{порт}} {{[-u|--username]}} {{пользователь}} {{[-i|--interactive]}}`
