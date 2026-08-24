# Clear-History

> Удалять записи из истории команд текущей сессии PowerShell.
> Примечание: в качестве псевдонима для `Clear-History` можно использовать `clhy`.
> Больше информации: <https://learn.microsoft.com/powershell/module/microsoft.powershell.core/clear-history>.

- Очистить всю историю команд текущей сессии:

`Clear-History`

- Удалить команды с указанным именем:

`Clear-History -CommandLine "{{команда}}"`

- Удалить несколько команд по имени:

`Clear-History -CommandLine {{"команда1", "команда2", ...}}`

- Удалить конкретную запись истории по ID:

`Clear-History -Id {{номер_id}}`

- Удалить несколько записей по ID:

`Clear-History -Id {{id1, id2, ...}}`

- Удалить команды в диапазоне ID:

`Clear-History -Id ({{начальный_id}}..{{конечный_id}})`

- Показать, что будет удалено:

`Clear-History -WhatIf`

- Запросить подтверждение перед очисткой:

`Clear-History -Confirm`
