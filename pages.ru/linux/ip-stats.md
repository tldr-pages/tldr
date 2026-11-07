# ip stats

> Показывать статистику интерфейсов и управлять ею.
> Больше информации: <https://manned.org/ip-stats>.

- Показать статистику всех сетевых интерфейсов:

`ip {{[st|stats]}}`

- Показать статистику конкретного сетевого интерфейса:

`ip {{[st|stats]}} show dev {{сетевой_интерфейс}}`

- Показать статистику канального уровня (аналог `ip -statistics link show`):

`ip {{[st|stats]}} show group link`

- Показать статистику аппаратной разгрузки для всех устройств:

`ip {{[st|stats]}} show group offload`

- Показать статистику разгрузки для конкретного интерфейса:

`ip {{[st|stats]}} show dev {{сетевой_интерфейс}} group offload`

- Показать конкретную подгруппу разгрузки:

`ip {{[st|stats]}} show dev {{сетевой_интерфейс}} group offload subgroup {{l3_stats|cpu_hit|hw_stats_info}}`

- Показать статистику по семейству адресов (например, MPLS):

`ip {{[st|stats]}} show group afstats subgroup {{mpls}}`

- Включить сбор статистики аппаратного уровня L3 на устройстве:

`ip {{[st|stats]}} set dev {{сетевой_интерфейс}} l3_stats on`
