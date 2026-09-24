# gh codespace

> Подключаться к codespace и управлять ими в GitHub.
> Больше информации: <https://cli.github.com/manual/gh_codespace>.

- Создать codespace в GitHub в интерактивном режиме:

`gh {{[cs|codespace]}} create`

- Вывести список всех доступных codespace:

`gh {{[cs|codespace]}} {{[ls|list]}}`

- Подключиться к codespace по SSH в интерактивном режиме:

`gh {{[cs|codespace]}} ssh`

- Передать указанный файл в codespace в интерактивном режиме:

`gh {{[cs|codespace]}} cp {{путь/к/исходному_файлу}} remote:{{путь/к/удалённому_файлу}}`

- Вывести список портов codespace в интерактивном режиме:

`gh {{[cs|codespace]}} ports`

- Вывести логи codespace в интерактивном режиме:

`gh {{[cs|codespace]}} logs`

- Удалить codespace в интерактивном режиме:

`gh {{[cs|codespace]}} delete`

- Показать справку по подкоманде:

`gh {{[cs|codespace]}} {{code|cp|create|delete|edit|...}} {{[-h|--help]}}`
