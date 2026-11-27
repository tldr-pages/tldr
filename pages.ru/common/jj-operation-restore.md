# jj operation restore

> Восстанавливать репозиторий к более раннему состоянию из журнала операций.
> Смотрите также: `jj undo`, `jj operation log`, `jj operation revert`, `jj operation show`.
> Больше информации: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-restore>.

- Восстановить состояние репозитория на момент конкретной операции:

`jj {{[op|operation]}} restore {{идентификатор_операции}}`

- Восстановить только состояние репозитория и локальные закладки (игнорируя удалённо-отслеживаемые закладки):

`jj {{[op|operation]}} restore --what repo {{идентификатор_операции}}`
