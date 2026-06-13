# npm find-dupes

> Определять дублирующиеся зависимости в `node_modules`.
> Больше информации: <https://docs.npmjs.com/cli/npm-find-dupes/>.

- Вывести список всех дублирующихся пакетов в `node_modules`:

`npm find-dupes`

- Включить `devDependencies` в обнаружение дубликатов:

`npm find-dupes --include dev`

- Вывести список всех дублирующихся экземпляров конкретного пакета в `node_modules`:

`npm find-dupes {{имя_пакета}}`

- Исключить опциональные зависимости из обнаружения дубликатов:

`npm find-dupes --omit optional`

- Установить уровень логирования для вывода:

`npm find-dupes --loglevel {{silent|error|warn|info|verbose}}`

- Вывести информацию о дубликатах в формате JSON:

`npm find-dupes --json`

- Ограничить поиск дубликатов определёнными областями:

`npm find-dupes --scope {{@scope1,@scope2}}`

- Исключить определённые области из обнаружения дубликатов:

`npm find-dupes --omit-scope {{@scope1,@scope2}}`
