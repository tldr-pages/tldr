# babel

> Un transpiler che converte codice JavaScript da sintassi ES6/ES7 ad ES5.
> Maggiori informazioni: <https://babeljs.io/>.

- Transpila uno specifico file e stampa il risultato su `stdout`:

`babel {{percorso/del/file}}`

- Transpila un file e scrivi il risultato su uno specifico file di output:

`babel {{percorso/del/file_input}} --out-file {{percorso/del/file_output}}`

- Transpila un file ogni volta che viene modificato:

`babel {{percorso/del/file}} --watch`

- Transpila un'intera directory di file:

`babel {{percorso/della/directory_input}}`

- Transpila un'intera directory ignorando specifici file separati da virgola:

`babel {{percorso/della/directory_input}} --ignore {{file_ignorati}}`

- Transpila minimizzando il codice JavaScript in output:

`babel {{percorso/del/file_input}} --minified`

- Scegli un insieme di preset per formattare l'output:

`babel {{percorso/del/file_input}} --presets {{preset}}`

- Mostra tutte le opzioni disponibili:

`babel --help`
