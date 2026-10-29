# pixiecore

> Управлять сетевой загрузкой машин.
> Больше информации: <https://github.com/danderson/netboot/tree/main/pixiecore>.

- Запустить PXE-сервер загрузки, предоставляющий загрузочный образ `netboot.xyz`:

`pixiecore {{quick}} xyz --dhcp-no-bind`

- Запустить новый PXE-сервер загрузки, предоставляющий загрузочный образ Ubuntu:

`pixiecore {{quick}} ubuntu --dhcp-no-bind`

- Вывести список всех доступных загрузочных образов для быстрого режима:

`pixiecore quick --help`
