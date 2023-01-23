# tsv-filter

> TSV fájl sorainak szűrése az egyes mezőkre vonatkozó tesztek futtatásával. További információ: <https://github.com/eBay/tsv-utils#tsv-filter>.

- Kinyomtatja azokat a sorokat, amelyekben egy adott oszlop számszerűen megegyezik egy adott számmal:

`tsv-filter -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`

- Azoknak a soroknak a kiírása, ahol egy adott oszlop \[eq\]ual/\[n\]on \[e\]qual/\[l\]ess \[t\]han/\[l\]ess mint vagy \[e\]qual/\[g\]reater \[t\]han/\[g\]reater mint vagy \[e\]qual egy adott számmal:

`tsv-filter --{{eq|ne|lt|le|gt|ge}} {{column_number}}:{{number}} {{path/to/tsv_file}}`

- Kinyomtatja azokat a sorokat, ahol egy adott oszlop \[eq\]ual/\[n\]ot \[e\]qual/rész/nem része egy adott karakterláncnak:

`tsv-filter --str-{{eq|ne|in-fld|not-in-fld}} {{column_number}}:{{string}} {{path/to/tsv_file}}`

- Szűrés a nem üres mezőkre:

`tsv-filter --not-empty {{column_number}} {{path/to/tsv_file}}`

- Azoknak a soroknak a nyomtatása, ahol egy adott oszlop üres:

`tsv-filter --invert --not-empty {{column_number}} {{path/to/tsv_file}}`

- Azoknak a soroknak a nyomtatása, amelyek két feltételnek megfelelnek:

`tsv-filter --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- Legalább egy feltételnek megfelelő sorok nyomtatása:

`tsv-filter --or --eq {{column_number1}}:{{number}} --str-eq {{column_number2}}:{{string}} {{path/to/tsv_file}}`

- Megszámolja az egyező sorokat, az első sort \[H\]eader-ként értelmezve:

`tsv-filter --count -H --eq {{field_name}}:{{number}} {{path/to/tsv_file}}`
