# vnstati

> Suport de ieșire imagine PNG pentru VnStat.
> Mai multe informaţii: <https://manned.org/vnstati>

- Ieșiți un rezumat al ultimelor 2: luni, zile și toate timpurile:

`vnstati --summary --iface {{network_interface}} --output {{path/to/output.png}}`

- Ieșire cele mai mari 10 zile de trafic intensiv din toate timpurile:

`vnstati --top10 --iface {{network_interface}} --output {{path/to/output.png}}`

- Date statistice lunare de trafic din ultimele 12 luni:

`vnstati --months --iface {{network_interface}} --output {{path/to/output.png}}`

- Statisticile de trafic orar din ultimele 24 de ore:

`vnstati --hours --iface {{network_interface}} --output {{path/to/output.png}}`
