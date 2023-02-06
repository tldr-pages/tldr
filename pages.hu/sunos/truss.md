# truss

> Hibaelhárító eszköz a rendszerhívások nyomon követésére. A strace SunOS megfelelője. További információ: <https://www.unix.com/man-page/linux/1/truss>.

- Egy program nyomon követése a program végrehajtásával kezdődik, követve az összes gyermekfolyamatot:

`truss -f {{program}}`

- Egy adott folyamat nyomon követésének megkezdése annak PID-je alapján:

`truss -p {{pid}}`

- Egy program nyomon követésének megkezdése a program végrehajtásával, az argumentumok és a környezeti változók megjelenítésével:

`truss -a -e {{program}}`

- Számolja az időt, a hívásokat és a hibákat minden egyes rendszerhívásnál, és a program kilépésekor összefoglaló jelentést készít:

`truss -c -p {{pid}}`

- Egy folyamat nyomon követése a kimenet szűrésével rendszerhívásonként:

`truss -p {{pid}} -t {{system_call_name}}`
