# black

> Un formattatore automatico di codice Python.
> Maggiori informazioni: <https://github.com/psf/black>.

- Auto-formatta un file o un'intera cartella:

`black {{percorso/a/file_o_cartella}}`

- Formatta il codice che gli viene passato come stringa:

`black -c "{{codice}}"`

- Mostra i cambiamenti che verrebbero applicati a ciascun file:

`black --diff {{percorso/a/file_o_cartella}}`

- Verifica se i file necessitano di auto-formattazione senza modificare nulla:

`black --check {{percorso/a/file_o_cartella}}`

- Auto-formatta un file o una cartella senza produrre output:

`black --quiet {{percorso/a/file_o_cartella}}`

- Auto-formatta un file o una cartella senza sostituire gli apici con le doppie virgolette:

`black --skip-string-normalization {{percorso/a/file_o_cartella}}`
