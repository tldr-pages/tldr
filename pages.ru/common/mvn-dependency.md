# mvn dependency

> Управлять зависимостями проекта Maven и анализировать их.
> Предоставляет цели для просмотра, разрешения и копирования зависимостей проекта.
> Больше информации: <https://maven.apache.org/plugins/maven-dependency-plugin/usage.html>.

- Добавить зависимость:

`mvn dependency:add -Dgav={{id_группы}}:{{id_артефакта}}:{{версия}}`

- Показать полное дерево зависимостей, включая прямые и транзитивные зависимости:

`mvn dependency:tree`

- Проанализировать зависимости и выделить неиспользуемые или необъявленные:

`mvn dependency:analyze`

- Скопировать все зависимости проекта (по умолчанию в `target/dependency/`):

`mvn dependency:copy-dependencies`

- Разрешить и загрузить все зависимости проекта в локальный репозиторий Maven:

`mvn dependency:resolve`

- Принудительно обновить все зависимости из удалённых репозиториев:

`mvn dependency:resolve {{[-U|--update-snapshots]}}`
