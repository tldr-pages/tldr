# chown

> Cambia la proprietà di utente e gruppo di file e directory.
> Vedi anche: `chgrp`.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/chown-invocation.html>.

- Cambia l'utente proprietario di un file/directory:

`sudo chown {{utente}} {{percorso/del/file_o_directory}}`

- Cambia l'utente proprietario e il gruppo di un file/directory:

`sudo chown {{utente}}:{{gruppo}} {{percorso/del/file_o_directory}}`

- Cambia sia l'utente proprietario che il gruppo in entrambi i casi con lo stesso nome `utente`:

`sudo chown {{utente}}: {{percorso/del/file_o_directory}}`

- Cambia il gruppo di un file in un gruppo a cui l'utente corrente appartiene:

`chown :{{gruppo}} {{percorso/del/file_o_directory}}`

- Cambia ricorsivamente il proprietario di una directory e dei suoi contenuti:

`sudo chown {{[-R|--recursive]}} {{utente}} {{percorso/della/directory}}`

- Cambia il proprietario di un link simbolico:

`sudo chown {{[-h|--no-dereference]}} {{utente}} {{percorso/del/link_simbolico}}`

- Cambia il proprietario di un file/directory in modo che coincida con un file di riferimento:

`sudo chown --reference {{percorso/del/file_riferimento}} {{percorso/del/file_o_directory}}`
