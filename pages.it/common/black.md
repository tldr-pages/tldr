# black

> Un formattatore automatico di codice Python.
> Maggiori informazioni: <https://black.readthedocs.io/en/stable/usage_and_configuration/the_basics.html>.

- Auto-formatta un file o un'intera directory:

`black {{percorso/del/file_o_directory}}`

- Formatta il codice che gli viene passato come stringa:

`black -c "{{codice}}"`

- Verifica se i file necessitano di auto-formattazione senza modificare nulla:

`black --check {{percorso/del/file_o_directory}}`

- Mostra i cambiamenti che verrebbero applicati a ciascun file:

`black --diff {{percorso/del/file_o_directory}}`

- Auto-formatta un file o una directory senza produrre output:

`black --quiet {{percorso/del/file_o_directory}}`

- Auto-formatta un file o una directory senza sostituire gli apici con le doppie virgolette:

`black --skip-string-normalization {{percorso/del/file_o_directory}}`
