# dbus-daemon

> A D-Bus üzenetküldő démon, amely lehetővé teszi több program számára az üzenetváltást. További információ: <https://www.freedesktop.org/wiki/Software/dbus/>.

- A démon futtatása egy konfigurációs fájl segítségével:

`dbus-daemon --config-file {{path/to/file}}`

- A démon futtatása a szokásos, bejelentkezési munkamenetenkénti üzenetbusz-konfigurációval:

`dbus-daemon --session`

- A démon futtatása az egész rendszerre kiterjedő szabványos üzenetbusz-konfigurációval:

`dbus-daemon --system`

- Állítsa be a hallgatni kívánt címet, és írja felül a hozzá tartozó konfigurációs értéket:

`dbus-daemon --address {{address}}`

- A folyamat azonosítójának kiadása a `stdout` címre:

`dbus-daemon --print-pid`

- Kényszerítse az üzenőbuszt, hogy az üzeneteket a rendszer naplójába írja:

`dbus-daemon --syslog`
