# jj operation abandon

> Отбрасывать историю операций в репозитории `jj`.
> Смотрите также: `jj operation log`, `jj operation restore`, `jj operation revert`.
> Больше информации: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-operation-abandon>.

- Отбросить конкретную операцию:

`jj {{[op|operation]}} abandon {{идентификатор_операции}}`

- Отбросить конкретную операцию и всех её предков:

`jj {{[op|operation]}} abandon ..{{идентификатор_операции}}`

- Отбросить недавние операции после восстановления к более раннему состоянию:

`jj {{[op|operation]}} abandon {{идентификатор_операции}}..@-`
