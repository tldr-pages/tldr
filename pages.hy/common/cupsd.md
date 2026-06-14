# բաժակ

> Սերվերի դեյմոն CUPS տպագիր սերվերի համար:.
> Լրացուցիչ տեղեկություններ. <https://openprinting.github.io/cups/doc/man-cupsd.html>:.

- Սկսեք `cupsd`-ը հետին պլանում, այսինքն: որպես դևոն:

`cupsd`

- Սկսեք `cupsd`-ը [f]առաջին պլանում՝:

`cupsd -f`

- [l]գործարկել `cupsd` ըստ պահանջի (սովորաբար օգտագործվում է `launchd`-ի կամ `systemd`-ի կողմից):

`cupsd -l`

- Սկսեք `cupsd`-ը՝ օգտագործելով նշված `cupsd.conf` [c] կազմաձևման ֆայլը՝:

`cupsd -c {{path/to/cupsd.conf}}`

- Սկսեք `cupsd`-ը՝ օգտագործելով նշված `cups-files.conf` կազմաձևման ֆայլը՝:

`cupsd -s {{path/to/cups-files.conf}}`

- [t]ստուգեք `cupsd.conf` [c] կազմաձևման ֆայլը սխալների համար՝:

`cupsd -t -c {{path/to/cupsd.conf}}`

- [t]ստուգեք `cups-files.conf` կազմաձևման ֆայլը սխալների համար՝:

`cupsd -t -s {{path/to/cups-files.conf}}`

- Ցուցադրել [h] օգնություն:

`cupsd -h`
