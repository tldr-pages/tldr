# expand

> Converti caratteri tab in spazi.

- Converti tab in un file in spazi, scrivendo su standard output:

`expand {{file}}`

- Converti i tab in spazi, leggendo da standard input:

`expand`

- Non convertire i tab dopo caratteri di spaziatura:

`expand -i {{file}}`

- Sostituisci i tab con un determinato numeroo di spazi, non 8 (default):

`expand -t={{numero_spazi}} {{file}}`

- Utilizza una lista separata da virgole di posizioni esplicite di tab:

`expand -t={{1,4,6}}`
