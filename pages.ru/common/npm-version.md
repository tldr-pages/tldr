# npm version

> Увеличивать версию Node.js-пакета.
> Больше информации: <https://docs.npmjs.com/cli/npm-version/>.

- Показать версию:

`npm version`

- Увеличить минорную версию:

`npm version minor`

- Установить определённую версию:

`npm version {{версия}}`

- Увеличить патч-версию без создания Git-тега:

`npm version patch --no-git-tag-version`

- Увеличить мажорную версию с пользовательским сообщением коммита:

`npm version major {{[-m|--message]}} "{{Обновление до %s по причинам}}"`
