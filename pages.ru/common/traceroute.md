# traceroute

> Выводить маршрут следования пакетов до сетевого хоста.
> Смотрите также: `mtr`.
> Больше информации: <https://manned.org/traceroute>.

- Выполнить трассировку до хоста:

`traceroute {{example.com}}`

- Отключить преобразование IP-адресов в имена хостов:

`traceroute -n {{example.com}}`

- Указать время ожидания ответа в секундах:

`traceroute {{[-w|--wait]}} {{0.5}} {{example.com}}`

- Указать количество запросов на каждый узел (hop):

`traceroute {{[-q|--queries]}} {{5}} {{example.com}}`

- Указать размер отправляемого пакета в байтах:

`traceroute {{example.com}} {{42}}`

- Определить MTU до узла назначения:

`traceroute --mtu {{example.com}}`

- Использовать протокол ICMP вместо UDP для трассировки:

`traceroute {{[-I|--icmp]}} {{example.com}}`
