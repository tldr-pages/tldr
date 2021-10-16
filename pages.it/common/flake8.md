# flake8

> Programma per verificare lo stile e la qualità di un codice Python.
> Maggiori informazioni: <https://flake8.pycqa.org/>.

- Analizza ricorsivamente un file o una cartella:

`flake8 {{percorso/a/file_o_cartella}}`

- Analizza ricorsivamente un file o una cartella e mostra le righe contenenti errori:

`flake8 --show-source {{percorso/a/file_o_cartella}}`

- Analizza ricorsivamente un file o una cartella e ignora la lista delle regole specificate. (La lista con tutte le regole è consultabile su flake8rules.com):

`flake8 --ignore {{regola1,regola2}} {{percorso/a/file_o_cartella}}`

- Analizza ricorsivamente un file o una cartella ma esclude i file che corrispondono a una sottostringa o a un glob:

`flake8 --exclude {{sottostringa1,glob2}} {{percorso/a/file_o_cartella}}`
