# emacsclient

> Apri file in un server emacs esistente.
> Maggiori informazioni: <https://www.emacswiki.org/emacs/EmacsClient>.

- Apri un file in un server Emacs esistente (utilizzando la GUI se disponibile):

`emacsclient {{nome_file}}`

- Apri un file in modalità console (senza finestra X):

`emacsclient -nw {{nome_file}}`

- Apri un file in un frame Emacs esistente e ritorna immediatamente:

`emacsclient -n {{nome_file}}`
