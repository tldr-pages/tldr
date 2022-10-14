# chgrp

> Cambia il gruppo proprietario di file e cartelle.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/chgrp>.

- Cambia il gruppo proprietario di un file/directory:

`chgrp {{gruppo}} {{percorso/al/file}}`

- Cambia ricorsivamente il gruppo proprietario di una directory e dei suoi contenuti:

`chgrp -R {{gruppo}} {{percorso/a/directory}}`

- Cambia il gruppo proprietario di un link simbolico:

`chgrp -h {{gruppo}} {{path/to/symlink}}`

- Cambia il gruppo proprietario di un file/directory rendendolo uguale a quello di un altro file di riferimento:

`chgrp --reference={{percorso/al/file_riferimento}} {{percorso/al/file}}`
