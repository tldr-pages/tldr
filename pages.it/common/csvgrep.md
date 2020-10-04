# csvgrep

> Filtra righe CSV con stringhe e pattern matching.
> Incluso in csvkit.
> Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- Trova righe contenenti una certa stringa nella colonna 1:

`csvgrep -c {{1}} -m {{stringa}} {{data.csv}}`

- Trova righe per le quali le colonne 3 e 4 soddisfano una certa regex:

`csvgrep -c {{3,4}} -r {{pattern_regex}} {{data.csv}}`

- Trova righe dove la colonna "nome" NON include la stringa "Mario Rossi":

`csvgrep -i -c {{nome}} -m "{{Mario Rossi}}" {{data.csv}}`
