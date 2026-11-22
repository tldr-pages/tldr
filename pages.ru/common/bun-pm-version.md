# bun pm version

> Управлять полем `version` в `package.json`.
> Больше информации: <https://bun.com/docs/pm/cli/pm#version>.

- Показать текущую версию пакета:

`bun pm version`

- Установить конкретную версию:

`bun pm version {{9.0.1}}`

- Увеличить версию по типу семантического версионирования:

`bun pm version {{major|minor|patch|premajor|preminor|prepatch|prerelease}}`

- Установить версию на основе тегов Git:

`bun pm version from-git`
