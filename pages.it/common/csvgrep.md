# csvgrep

> Filtra righe CSV con stringhe e pattern matching.
> Incluso in csvkit.
> Maggiori informazioni: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- Trova righe contenenti una certa stringa nella colonna 1:

`csvgrep {{[-c|--columns]}} {{1}} {{[-m|--match]}} {{stringa}} {{data.csv}}`

- Trova righe per le quali le colonne 3 e 4 soddisfano una certa espressione regolare:

`csvgrep {{[-c|--columns]}} {{3,4}} {{[-r|--regex]}} {{espressione_regolare}} {{data.csv}}`

- Trova righe dove la colonna "nome" NON include la stringa "Mario Rossi":

`csvgrep {{[-i|--invert-match]}} {{[-c|--columns]}} {{nome}} {{[-m|--match]}} "{{Mario Rossi}}" {{data.csv}}`
