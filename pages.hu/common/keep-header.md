# keep-header

> Az első sort nem érinti a parancs, közvetlenül a `stdout` címre továbbítja. További információ: <https://github.com/eBay/tsv-utils#keep-header>.

- Rendezzen egy fájlt, és tartsa az első sort a tetején:

`keep-header {{path/to/file}} -- sort`

- Az első sort közvetlenül a `stdout` címre adja ki, a fájl többi részét átadja a megadott parancsnak:

`keep-header {{path/to/file}} -- {{command}}`

- Olvassa be a `stdin`, az első sor kivételével az egészet rendezve:

`cat {{path/to/file}} | keep-header -- {{command}}`

- Grep egy fájl, az első sor megtartása a keresési mintától függetlenül:

`keep-header {{path/to/file}} -- grep {{pattern}}`
