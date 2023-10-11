# chgrp

> Cambia il gruppo proprietario di file e directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/chgrp>.

- Cambia il gruppo proprietario di un file/directory:

`chgrp {{gruppo}} {{percorso/del/file}}`

- Cambia ricorsivamente il gruppo proprietario di una directory e dei suoi contenuti:

`chgrp -R {{gruppo}} {{percorso/della/directory}}`

- Cambia il gruppo proprietario di un link simbolico:

`chgrp -h {{gruppo}} {{percorso/del/symlink}}`

- Cambia il gruppo proprietario di un file/directory rendendolo uguale a quello di un altro file di riferimento:

`chgrp --reference={{percorso/del/file_riferimento}} {{percorso/del/file}}`
