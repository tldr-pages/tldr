# mvn idea

> Генерировать файлы проекта IntelliJ IDEA (`.ipr`, `.iml` и `.iws`) для проекта Maven.
> Примечание: этот плагин устарел. Он больше не поддерживается.
> Больше информации: <https://maven.apache.org/plugins/maven-idea-plugin/usage.html>.

- Сгенерировать все файлы проекта IntelliJ IDEA:

`mvn idea:idea`

- Сгенерировать только файл проекта (`.ipr`):

`mvn idea:project`

- Сгенерировать только файл рабочей области (`.iws`):

`mvn idea:workspace`

- Сгенерировать только файлы модуля (`.iml`):

`mvn idea:module`

- Удалить все сгенерированные файлы проекта:

`mvn idea:clean`
