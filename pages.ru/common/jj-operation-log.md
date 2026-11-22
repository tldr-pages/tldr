# jj operation log

> Показывать журнал операций в репозитории `jj`.
> Больше информации: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-log>.

- Показать журнал операций:

`jj {{[op|operation]}} log`

- Ограничить количество отображаемых операций:

`jj {{[op|operation]}} log {{[-n|--limit]}} {{количество}}`

- Показать операции в обратном порядке (сначала самые старые):

`jj {{[op|operation]}} log --reversed`

- Показать операции без графа:

`jj {{[op|operation]}} log {{[-G|--no-graph]}}`

- Отобразить журнал операций с использованием пользовательского шаблона:

`jj {{[op|operation]}} log {{[-T|--template]}} "{{шаблон}}"`
