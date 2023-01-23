# vnstati

> PNG kép kimeneti támogatása a vnStat számára. További információ: <https://manned.org/vnstati>.

- Az elmúlt 2: hónapok, napok és minden idők összefoglalójának kimenete:

`vnstati --summary --iface {{network_interface}} --output {{path/to/output.png}}`

- Minden idők 10 legforgalmasabb napjának kimenete:

`vnstati --top10 --iface {{network_interface}} --output {{path/to/output.png}}`

- Az elmúlt 12 hónap havi forgalmi statisztikáinak kiadása:

`vnstati --months --iface {{network_interface}} --output {{path/to/output.png}}`

- Óránkénti forgalmi statisztikák kiadása az elmúlt 24 órából:

`vnstati --hours --iface {{network_interface}} --output {{path/to/output.png}}`
