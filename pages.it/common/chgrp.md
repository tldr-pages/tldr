# chgrp

> Cambia il gruppo proprietario di file e cartelle.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/chgrp>.

- Cambia il gruppo proprietario di un file/cartella:

`chgrp {{gruppo}} {{percorso/del/file}}`

- Cambia ricorsivamente il gruppo proprietario di una cartella e dei suoi contenuti:

`chgrp -R {{gruppo}} {{percorso/della/cartella}}`

- Cambia il gruppo proprietario di un link simbolico:

`chgrp -h {{gruppo}} {{path/to/symlink}}`

- Cambia il gruppo proprietario di un file/cartella rendendolo uguale a quello di un altro file di riferimento:

`chgrp --reference={{percorso/del/file_riferimento}} {{percorso/del/file}}`
