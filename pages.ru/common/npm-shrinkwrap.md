# npm shrinkwrap

> Фиксировать зависимости пакета, создавая файл `npm-shrinkwrap.json`.
> Аналогичен `package-lock.json`, но используется для опубликованных пакетов.
> Больше информации: <https://docs.npmjs.com/cli/shrinkwrap/>.

- Сгенерировать файл `npm-shrinkwrap.json` из текущего `package-lock.json`:

`npm shrinkwrap`

- Сгенерировать файл, исключая devDependencies (режим продакшн):

`npm shrinkwrap --production`

- Принудительно создать файл, даже если он уже существует:

`npm shrinkwrap --force`
