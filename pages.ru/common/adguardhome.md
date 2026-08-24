# AdGuardHome

> Программное обеспечение для блокировки рекламы и отслеживания во всей сети.
> Больше информации: <https://github.com/AdguardTeam/AdGuardHome>.

- Запустить AdGuard Home:

`AdGuardHome`

- Запустить AdGuard с заданной конфигурацией:

`AdGuardHome --config {{путь/к/AdGuardHome.yaml}}`

- Установить рабочий каталог, где будут сохраняться данные:

`AdGuardHome --work-dir {{путь/к/каталогу}}`

- Установить или удалить AdGuard Home как службу:

`AdGuardHome --service {{install|uninstall}}`

- Запустить службу AdGuard Home:

`AdGuardHome --service start`

- Перезагрузить конфигурацию для службы AdGuard Home:

`AdGuardHome --service reload`

- Остановить или перезапустить службу AdGuard Home:

`AdGuardHome --service {{stop|restart}}`
