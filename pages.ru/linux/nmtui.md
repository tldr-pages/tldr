# nmtui

> Текстовый интерфейс для управления NetworkManager.
> Используйте `<стрелки>` для навигации, `<Enter>` для выбора.
> Смотрите также: `nmcli`.
> Больше информации: <https://networkmanager.pages.freedesktop.org/NetworkManager/NetworkManager/nmtui.html>.

- Открыть пользовательский интерфейс:

`nmtui`

- Показать список доступных подключений с возможностью их активации или деактивации:

`nmtui connect`

- Подключиться к указанной сети:

`nmtui connect {{имя|uuid|устройство|SSID}}`

- Отредактировать/Добавить/Удалить указанную сеть:

`nmtui edit {{имя|id}}`

- Задать имя хоста системы:

`nmtui hostname`
