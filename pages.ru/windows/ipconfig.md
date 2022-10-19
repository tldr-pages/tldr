# ipconfig

> Отображение и управление сетевыми настройками Windows.
> Больше информации: <https://learn.microsoft.com/windows-server/administration/windows-commands/ipconfig>.

- Показать список сетевых адаптеров:

`ipconfig`

- Показать подробный список сетевых адаптеров:

`ipconfig /all`

- Обновить IP-адреса сетевого адаптера:

`ipconfig /renew {{адаптер}}`

- Освободить IP-адреса сетевого адаптера:

`ipconfig /release {{адаптер}}`

- Удалить все данные из кеша DNS:

`ipconfig /flushdns`
