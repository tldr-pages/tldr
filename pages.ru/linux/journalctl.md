# journalctl

> Запрашивать записи из журнала systemd.
> Смотрите также: `dmesg`.
> Больше информации: <https://www.freedesktop.org/software/systemd/man/latest/journalctl.html>.

- Показать последние `n` строк и отслеживать новые сообщения (аналогично `tail --follow` для традиционного syslog):

`journalctl {{[-n|--lines]}} {{n}} {{[-f|--follow]}}`

- Показать все сообщения с уровнем приоритета 3 (ошибки) с предпоследней загрузки:

`journalctl {{[-b|--boot]}} -1 {{[-p|--priority]}} 3`

- Показать все сообщения от определённого юнита:

`journalctl {{[-u|--unit]}} {{юнит}}`

- Показать логи для указанного юнита с момента его последнего запуска:

`journalctl _SYSTEMD_INVOCATION_ID=$(systemctl show --value --property=InvocationID {{юнит}})`

- Отфильтровать сообщения по временному диапазону (метка времени или заполнители, такие как "yesterday"):

`journalctl {{[-S|--since]}} {{now|today|yesterday|tomorrow|...}} {{[-U|--until]}} "{{ГГГГ-ММ-ДД ЧЧ:ММ:СС}}"`

- Показать все сообщения от определённого процесса:

`journalctl _PID={{pid}}`

- Показать все сообщения от определённого исполняемого файла:

`journalctl {{путь/к/исполняемому_файлу}}`

- Удалить записи журнала старше 2 дней:

`journalctl --vacuum-time 2d`
