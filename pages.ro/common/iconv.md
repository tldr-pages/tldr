# iconv

> Convertește textul dintr-o codificare în alta.

- Conversia fișierului la o codificare specifică și imprimarea la stdout:

`iconv -f {{from_encoding}} -t {{to_encoding}} {{input_file}}`

- Conversia fișierului la codificarea locală curentă și ieșirea într-un fișier:

`iconv -f {{from_encoding}} {{input_file}} > {{output_file}}`

- Lista codificărilor acceptate:

`iconv -l`
