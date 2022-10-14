# babel

> Un transpiler che converte codice JavaScript da sintassi ES6/ES7 ad ES5.
> Maggiori informazioni: <https://babeljs.io/>.

- Transpila uno specifico file e stampa il risultato su stdout:

`babel {{percorso/al/file}}`

- Transpila un file e scrivi il risultato su uno specifico file di output:

`babel {{percorso/al/file_input}} --out-file {{percorso/al/file_output}}`

- Transpila un file ogni volta che viene modificato:

`babel {{percorso/al/file}} --watch`

- Transpila un'intera cartella di file:

`babel {{percorso/a/cartella_input}}`

- Transpila un'intera cartella ignorando specifici file separati da virgola:

`babel {{percorso/a/cartella_input}} --ignore {{file_ignorati}}`

- Transpila minimizzando il codice JavaScript in output:

`babel {{percorso/al/file_input}} --minified`

- Scegli un insieme di preset per formattare l'output:

`babel {{percorso/al/file_input}} --presets {{preset}}`

- Mostra tutte le opzioni disponibili:

`babel --help`
