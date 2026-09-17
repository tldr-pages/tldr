# npm dedupe

> Уменьшать дублирование в каталоге `node_modules`.
> Больше информации: <https://docs.npmjs.com/cli/npm-dedupe/>.

- Дедуплицировать пакеты в `node_modules`:

`npm {{[ddp|dedupe]}}`

- Следовать `package-lock.json` или `npm-shrinkwrap.json` при дедупликации:

`npm {{[ddp|dedupe]}} --lock`

- Запустить дедупликацию в строгом режиме:

`npm {{[ddp|dedupe]}} --strict`

- Пропустить опциональные/peer зависимости при дедупликации:

`npm {{[ddp|dedupe]}} --omit {{optional|peer}}`

- Включить подробное логирование для отладки:

`npm {{[ddp|dedupe]}} --loglevel verbose`

- Ограничить дедупликацию указанным пакетом:

`npm {{[ddp|dedupe]}} {{имя_пакета}}`
