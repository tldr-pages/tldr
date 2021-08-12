# json5

> Un instrument de linie de comandă pentru conversia fișierelor JSON5 în JSON.
> Mai multe informaţii: <https://json5.org>

- Conversia JSON5 stdin la JSON stdout:

`echo {{input}} | json5`

- Convertiți un fișier JSON5 la JSON și ieșiți la stdout:

`json5 {{path/to/input_file.json5}}`

- Conversia unui fișier JSON5 în fișierul JSON specificat:

`json5 {{path/to/input_file.json5}} --out-file {{path/to/output_file.json}}`

- Validează un fișier JSON5:

`json5 {{path/to/input_file.json5}} --validate`

- Specificați numărul de spații de indentat cu (sau „t” pentru file):

`json5 --space {{indent_amount}}`

- Vizualizaţi opţiunile disponibile:

`json5 --help`
