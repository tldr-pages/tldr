# AdGuardHome

> Программное обеспечение для блокировки рекламы и отслеживания во всей сети.
> Больше информации: <https://github.com/AdguardTeam/AdGuardHome>.

- Запустить AdGuard Home:

`AdGuardHome`

- Запустить AdGuard с заданной конфигурацией:

`AdGuardHome --config {{путь/до/AdGuardHome.yaml}}`

- Установить рабочую папку, где будут сохранятья данные:

`AdGuardHome --work-dir {{путь/до/папки}}`

- Установить или удалить AdGuard Home как службу:

`AdGuardHome --service {{install|uninstall}}`

- Запустить службу AdGuard Home:

`AdGuardHome --service start`

- Перезагрузить конфигурацию для службы AdGuard Home:

`AdGuardHome --service reload`

- Остановить или перезапустить службу AdGuard Home:

`AdGuardHome --service {{stop|restart}}`
