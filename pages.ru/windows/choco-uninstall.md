# choco uninstall

> Удалять пакеты с помощью Chocolatey.
> Больше информации: <https://docs.chocolatey.org/en-us/choco/commands/uninstall/>.

- Удалить один или несколько пакетов:

`choco uninstall {{пакет1 пакет2 ...}}`

- Удалить определённую версию пакета:

`choco uninstall {{пакет}} --version {{версия}}`

- Автоматически подтвердить все запросы:

`choco uninstall {{пакет}} --yes`

- Удалить все зависимости при удалении:

`choco uninstall {{пакет}} --remove-dependencies`

- Удалить все пакеты:

`choco uninstall all`
