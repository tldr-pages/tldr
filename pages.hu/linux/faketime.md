# faketime

> Egy adott parancs rendszeridejének meghamisítása. További információ: <https://manned.org/faketime>.

- Az idő hamisítása ma estére, mielőtt a `date` parancs eredményét kinyomtatná:

`faketime '{{today 23:30}}' {{date}}`

- Nyisson egy új `bash` héjat, amely a tegnapi napot használja aktuális dátumként:

`faketime '{{yesterday}}' {{bash}}`

- Szimulálja, hogyan viselkedne egy program jövő péntek este:

`faketime '{{next Friday 1 am}}' {{path/to/program}}`
