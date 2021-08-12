# dstat

> Instrument versatil pentru generarea statisticilor privind resursele sistemului.
> Mai multe informaţii: <http://dag.wieers.com/home-made/dstat>

- Afișează statistici CPU, disc, net, paging și sistem:

`dstat`

- Afișează statistici la fiecare 5 secunde și 4 actualizări numai:

`dstat {{5}} {{4}}`

- Afișează numai statistici CPU și memorie:

`dstat --cpu --mem`

- Listează toate pluginurile dstat disponibile:

`dstat --list`

- Afișați procesul utilizând cea mai mare memorie și cea mai mare CPU:

`dstat --top-mem --top-cpu`

- Afișează procentul bateriei și timpul rămas al bateriei:

`dstat --battery --battery-remain`
