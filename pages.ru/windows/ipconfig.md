# ipconfig

> Отображать и управлять сетевыми настройками Windows.
> Больше информации: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Показать список сетевых адаптеров:

`ipconfig`

- Показать подробный список сетевых адаптеров:

`ipconfig /all`

- Обновить IP-адреса для сетевого адаптера:

`ipconfig /renew {{адаптер}}`

- Освободить IP-адреса для сетевого адаптера:

`ipconfig /release {{адаптер}}`

- Показать локальный кеш DNS:

`ipconfig /displaydns`

- Удалить все данные из локального кеша DNS:

`ipconfig /flushdns`
