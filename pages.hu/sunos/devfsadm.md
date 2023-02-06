# devfsadm

> Adminisztrációs parancs a `/dev` oldalon. A `/dev` névtér karbantartása. További információ: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Új lemezek keresése:

`devfsadm -c disk`

- A lógó /dev hivatkozások megtisztítása és új eszközök keresése:

`devfsadm -C -v`

- Száraz futtatás - kiadja, hogy mi változna, de nem végez módosításokat:

`devfsadm -C -v -n`
