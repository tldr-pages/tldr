# bluetoothd

> Daemon a bluetooth eszközök kezelésére. További információ: <https://manned.org/bluetoothd>.

- Indítsa el a démont:

`bluetoothd`

- Indítsa el a démont, bejelentkezés a `stdout` címen:

`bluetoothd --nodetach`

- Indítsa el a démont egy adott konfigurációs fájllal (alapértelmezett: `/etc/bluetooth/main.conf`):

`bluetoothd --configfile {{path/to/file}}`

- A démon indítása a `stderr` címre küldött verbóziskimenettel:

`bluetoothd --debug`

- A démon indítása a bluetoothd vagy a plugins forrásban lévő meghatározott fájlokból származó verbóziskimenettel:

`bluetoothd --debug={{path/to/file1}}:{{path/to/file2}}:{{path/to/file3}}`
