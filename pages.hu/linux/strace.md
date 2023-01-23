# strace

> Hibaelhárító eszköz a rendszerhívások nyomon követésére. További információ: <https://manned.org/strace>.

- Egy adott folyamat nyomon követésének megkezdése annak PID-je alapján:

`strace -p {{pid}}`

- Egy folyamat nyomon követése és a kimenet szűrése rendszerhívás szerint:

`strace -p {{pid}} -e {{system_call_name}}`

- Számolja az időt, a hívásokat és a hibákat minden egyes rendszerhíváshoz, és a program kilépésekor összefoglaló jelentést készít:

`strace -p {{pid}} -c`

- Minden egyes rendszerhívásra fordított idő megjelenítése:

`strace -p {{pid}} -T`

- Egy program nyomon követésének megkezdése a program végrehajtásával:

`strace {{program}}`

- Egy program fájlműveleteinek nyomon követése:

`strace -e trace=file {{program}}`
