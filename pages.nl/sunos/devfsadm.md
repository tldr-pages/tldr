# devfsadm

> Beheer `/dev`.
> Onderhoudt de `/dev`-namespace.
> Meer informatie: <https://www.unix.com/man-page/sunos/1m/devfsadm>.

- Scan naar nieuwe schijven:

`devfsadm -c disk`

- Ruim overblijvende `/dev`-links op en scan naar nieuwe toestellen:

`devfsadm -C -v`

- Simuleer wat er zou gebeuren, zonder wijzigingen door te voeren:

`devfsadm -C -v -n`
