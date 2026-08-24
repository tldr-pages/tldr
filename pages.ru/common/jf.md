# jf

> Взаимодействовать с продуктами JFrog, такими как Artifactory, Xray, Distribution, Pipelines и Mission Control.
> Больше информации: <https://jfrog.com/help/r/jfrog-applications-and-cli-documentation/jfrog-cli>.

- Добавить новую конфигурацию:

`jf config add`

- Показать текущую конфигурацию:

`jf config show`

- Найти артефакты в указанном репозитории и каталоге:

`jf rt search --recursive {{имя_репозитория}}/{{путь}}/`
