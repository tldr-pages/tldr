# npm sbom

> Генерировать спецификацию программных компонентов (SBOM) для Node.js-проекта.
> Больше информации: <https://docs.npmjs.com/cli/npm-sbom/>.

- Вывести список всех зависимостей в проекте:

`npm sbom`

- Исключить зависимости `dev` и `optional`:

`npm sbom --omit dev --omit optional`

- Сгенерировать SBOM на основе только `package-lock.json`:

`npm sbom --package-lock-only`
