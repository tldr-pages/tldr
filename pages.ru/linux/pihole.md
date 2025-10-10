# pihole

> Управлять DNS-сервером для блокировки рекламы Pi-hole.
> Больше информации: <https://docs.pi-hole.net/main/pihole-command>.

- Проверить статус Pi-hole:

`pihole status`

- Обновить Pi-hole и Gravity:

`sudo pihole {{[-up|updatePihole]}}`

- Запустить или остановить демона:

`pihole {{enable|disable}}`

- Обновить списки и очистить кэш без перезапуска DNS-сервера:

`pihole reloaddns`

- Обновить список доменов, раздающих рекламу:

`pihole {{[-g|updateGravity]}}`

- Разрешить или запретить указанный домен:

`pihole {{allow|deny}} {{example.com}}`

- Искать домен в списках:

`pihole {{[-q|query]}} {{example.com}}`

- Открыть лог подключений в реальном времени:

`pihole {{[-t|tail]}}`
