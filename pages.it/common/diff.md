# diff

> Confronta file e directory.
> Maggiori informazioni: <https://manned.org/diff>.

- Confronta due file (elenca cambiamenti necessari per trasformare `vecchio_file` in `nuovo_file`):

`diff {{vecchio_file}} {{nuovo_file}}`

- Confronta due file ignorando gli spazi:

`diff {{[-w|--ignore-all-space]}} {{vecchio_file}} {{nuovo_file}}`

- Confronta due file mostrando le differenze fianco a fianco:

`diff {{[-y|--side-by-side]}} {{vecchio_file}} {{nuovo_file}}`

- Confronta due file, mostrando le differenze in formato unificato (come `git diff`):

`diff {{[-u|--unified]}} {{vecchio_file}} {{nuovo_file}}`

- Confronta due directory ricorsivamente (mostra i nomi dei file/directory diversi e le differenze trai file):

`diff {{[-r|--recursive]}} {{old_directory}} {{new_directory}}`

- Confronta due directory mostrando solamente il nome dei file diversi:

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{old_directory}} {{new_directory}}`
