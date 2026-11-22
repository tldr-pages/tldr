# jj operation revert

> Отменять более раннюю операцию, применяя её обратное действие в репозитории `jj`.
> Смотрите также: `jj operation log`, `jj operation restore`.
> Больше информации: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-revert>.

- Отменить последнюю операцию:

`jj {{[op|operation]}} revert`

- Отменить конкретную операцию:

`jj {{[op|operation]}} revert {{идентификатор_операции}}`

- Отменить только состояние репозитория и локальные закладки операции:

`jj {{[op|operation]}} revert --what repo {{идентификатор_операции}}`
