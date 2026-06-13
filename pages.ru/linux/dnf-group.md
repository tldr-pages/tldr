# dnf group

> Управление виртуальными коллекциями пакетов в системах на базе Fedora.
> Больше информации: <https://dnf.readthedocs.io/en/latest/command_ref.html#group-command>.

- Показать список групп DNF с указанием статуса установки в таблице:

`dnf {{[grp|group]}} list`

- Показать информацию о группе DNF, включая репозиторий и опциональные пакеты:

`dnf {{[grp|group]}} info {{имя_группы}}`

- Установить группу DNF:

`dnf {{[grp|group]}} install {{имя_группы}}`

- Удалить группу DNF:

`dnf {{[grp|group]}} remove {{имя_группы}}`

- Обновить группу DNF:

`dnf {{[grp|group]}} upgrade {{имя_группы}}`
