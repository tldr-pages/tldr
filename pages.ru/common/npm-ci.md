# npm ci

> Выполнять чистую установку зависимостей `npm`-проекта для автоматизированных сред.
> Устанавливать пакеты на основе `package-lock.json` или `npm-shrinkwrap.json`.
> Больше информации: <https://docs.npmjs.com/cli/npm-ci/>.

- Установить зависимости проекта из `package-lock.json` или `npm-shrinkwrap.json`:

`npm ci`

- Установить зависимости проекта, пропуская указанный тип зависимостей:

`npm ci --omit {{dev|optional|peer}}`

- Установить зависимости проекта без выполнения pre-/post-скриптов, определённых в `package.json`:

`npm ci --ignore-scripts`
