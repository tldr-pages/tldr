# lebab

> Un modernizator JavaScript pentru transpiling cod la ES6/ES7.
> Transformările trebuie furnizate pentru toate exemplele.
> Mai multe informaţii: <https://github.com/lebab/lebab>

- Afișează o listă a transformărilor disponibile:

`lebab --help`

- Transpile folosind una sau mai multe transformări separate prin virgulă:

`lebab --transform {{transformation}}`

- Transpila un fișier la stdout:

`lebab {{path/to/input_file}}`

- Transpila un fișier la fișierul de ieșire specificat:

`lebab {{path/to/input_file}} --out-file {{path/to/output_file}}`

- Înlocuiți toate fișierele `.js` din directorul specificat, glob sau fișier:

`lebab --replace {{directory|glob|file}}`
