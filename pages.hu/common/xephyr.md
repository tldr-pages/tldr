# Xephyr

> X-alkalmazásként futó, egymásba ágyazott X-kiszolgáló. További információ: <https://manned.org/xserver-xephyr>.

- Hozzon létre egy fekete ablakot ":2" megjelenítési azonosítóval:

`Xephyr -br -ac -noreset -screen {{800x600}} {{:2}}`

- Indítson el egy X-alkalmazást az új képernyőn:

`DISPLAY=:2 {{command_name}}`
