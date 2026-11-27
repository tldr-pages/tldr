# nxc

> Инструмент для перечисления и эксплуатации сетевых сервисов.
> Некоторые подкоманды, такие как `smb`, имеют собственную документацию.
> Больше информации: <https://www.netexec.wiki/getting-started/selecting-and-using-a-protocol>.

- Вывести список доступных модулей для указанного протокола:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-L|--list-modules]}}`

- Вывести список параметров для указанного модуля:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{имя_модуля}} --options`

- Указать [o]пцию для модуля:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-M|--module]}} {{имя_модуля}} -o {{НАЗВАНИЕ_ОПЦИИ}}={{значение_опции}}`

- Показать параметры для указанного протокола:

`nxc {{smb|ssh|ldap|ftp|wmi|winrm|rdp|vnc|mssql}} {{[-h|--help]}}`
