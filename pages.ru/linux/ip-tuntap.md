# ip tuntap

> Управлять виртуальными сетевыми интерфейсами TUN/TAP.
> Больше информации: <https://baturin.org/docs/iproute2/#ip-tuntap>.

- Показать все существующие устройства TUN/TAP:

`ip {{[tunt|tuntap]}}`

- Создать устройство TUN с конкретным именем:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0}} {{[m|mode]}} {{[t|tun]}}`

- Создать устройство TAP с конкретным именем:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tap0}} {{[m|mode]}} {{[ta|tap]}}`

- Удалить устройство TUN или TAP:

`sudo ip {{[tunt|tuntap]}} {{[d|delete]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}}`

- Установить владельца (UID) устройства TUN/TAP:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}} {{[u|user]}} {{имя_пользователя}}`

- Установить владельца (UID) и группу (GID) устройства TUN/TAP:

`sudo ip {{[tunt|tuntap]}} {{[a|add]}} {{[d|dev]}} {{tun0|tap0}} {{[m|mode]}} {{tun|tap}} {{[u|user]}} {{имя_пользователя}} {{[g|group]}} {{имя_группы}}`
