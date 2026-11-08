# ip neighbor

> Подкоманда IP для управления таблицами соседей (ARP/NDP).
> Смотрите также: `arp-scan`.
> Больше информации: <https://manned.org/ip-neighbour>.

- Показать записи таблицы соседей (ARP):

`ip {{[n|neighbor]}}`

- Удалить записи из таблицы соседей на устройстве `ethX`:

`sudo ip {{[n|neighbor]}} {{[f|flush]}} dev {{ethX}}`

- Выполнить поиск соседа и вернуть запись о нём:

`ip {{[n|neighbor]}} {{[g|get]}} {{ip_адрес_поиска}} dev {{ethX}}`

- Добавить или удалить запись ARP для IP-адреса соседа на `ethX`:

`sudo ip {{[n|neighbor]}} {{add|delete}} {{ip_адрес}} lladdr {{mac_адрес}} dev {{ethX}} nud reachable`

- Изменить или заменить запись ARP для IP-адреса соседа на `ethX`:

`sudo ip {{[n|neighbor]}} {{change|replace}} {{ip_адрес}} lladdr {{новый_mac_адрес}} dev {{ethX}}`

- Показать только соседей IPv6 или IPv4:

`ip {{-6|-4}} {{[n|neighbor]}}`
