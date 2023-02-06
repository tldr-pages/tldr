# csvgrep

> CSV sorok szűrése karakterlánc- és mintaillesztéssel. A csvkit része. További információ: <https://csvkit.readthedocs.io/en/latest/scripts/csvgrep.html>.

- Olyan sorok keresése, amelyekben az 1. oszlopban egy bizonyos karakterlánc szerepel:

`csvgrep -c {{1}} -m {{string_to_match}} {{data.csv}}`

- Olyan sorok keresése, amelyekben a 3. vagy 4. oszlop megfelel egy bizonyos reguláris kifejezésnek:

`csvgrep -c {{3,4}} -r {{regular_expression}} {{data.csv}}`

- Olyan sorok keresése, amelyekben a "name" oszlopban NEM szerepel a "John Doe" karakterlánc:

`csvgrep -i -c {{name}} -m "{{John Doe}}" {{data.csv}}`
