# dnf module

> Управление модульностью пакетов.
> Больше информации: <https://dnf.readthedocs.io/en/latest/command_ref.html#module-command>.

- Просмотр общего обзора модульности:

`dnf module list`

- Просмотр модульности конкретной программы:

`dnf module list {{имя_пакета}}`

- Включить пакет:

`sudo dnf module enable {{имя_пакета}}:{{поток}}`

- Включить и установить конкретную версию:

`dnf module install {{имя_пакета}}:{{поток}}`
