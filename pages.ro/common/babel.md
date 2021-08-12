# babel

> Un transpiler care convertește codul din sintaxa JavaScript ES6/ES7 în sintaxa ES5.
> Mai multe informaţii: <https://babeljs.io/>

- Transpile un fișier de intrare specificat și ieșirea la stdout:

`babel {{path/to/file}}`

- Transpila un fișier de intrare specificat și de ieșire la un anumit fișier:

`babel {{path/to/input_file}} --out-file {{path/to/output_file}}`

- Transpila fișierul de intrare de fiecare dată când este schimbat:

`babel {{path/to/input_file}} --watch`

- Transpilează un întreg director de fișiere:

`babel {{path/to/input_directory}}`

- Ignorați fișierele separate prin virgulă într-un director:

`babel {{path/to/input_directory}} --ignore {{ignored_files}}`

- Transpile și ieșirea ca JavaScript minified:

`babel {{path/to/input_file}} --minified`

- Alegeți un set de presetări pentru formatarea ieșirii:

`babel {{path/to/input_file}} --presets {{presets}}`

- Ieșire toate opțiunile disponibile:

`babel --help`
