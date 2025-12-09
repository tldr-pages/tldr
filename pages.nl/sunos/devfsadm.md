# devfsadm

> Administratie commando voor `/dev`. Beheert de `/dev` namespace.
> Meer informatie: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Scannen voor nieuwe schijven:

`devfsadm -c disk`

- Opkuisen van overblijvende /dev links, en detectie van nieuwe toestellen:

`devfsadm -C -v`

- Dry-run - output van wat er zou veranderen, zonder deze door te voeren:

`devfsadm -C -v -n`
