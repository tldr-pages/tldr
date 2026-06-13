# expand

> Converti caratteri tab in spazi.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/expand-invocation.html>.

- Converti tab in un file in spazi, scrivendo su `stdout`:

`expand {{percorso/del/file}}`

- Converti i tab in spazi, leggendo da `stdin`:

`expand`

- Non convertire i tab dopo caratteri di spaziatura:

`expand {{[-i|--initial]}} {{percorso/del/file}}`

- Sostituisci i tab con un determinato numero di spazi, non 8 (default):

`expand {{[-t|--tabs]}} {{numero_spazi}} {{percorso/del/file}}`

- Utilizza una lista separata da virgole di posizioni esplicite di tab:

`expand {{[-t|--tabs]}} {{1,4,6}}`
