# diff

> Confronta file e directory.
> Maggiori informazioni: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Confronta due file (elenca cambiamenti necessari per trasformare `vecchio_file` in `nuovo_file`):

`diff {{vecchio_file}} {{nuovo_file}}`

- Confronta due file ignorando gli spazi:

`diff -w {{vecchio_file}} {{nuovo_file}}`

- Confronta due file mostrando le differenze fianco a fianco:

`diff -y {{vecchio_file}} {{nuovo_file}}`

- Confronta due file, mostrando le differenze in formato unificato (come `git diff`):

`diff -u {{vecchio_file}} {{nuovo_file}}`

- Confronta due directory ricorsivamente (mostra i nomi dei file/directory diversi e le differenze trai file):

`diff -r {{old_directory}} {{new_directory}}`

- Confronta due directory mostrando solamente il nome dei file diversi:

`diff -rq {{old_directory}} {{new_directory}}`
