# diff

> Confronta file e cartelle.
> Maggiori informazioni: <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Confronta due file (elenca cambiamenti necessari per trasformare `vecchio_file` in `nuovo_file`):

`diff {{vecchio_file}} {{nuovo_file}}`

- Confronta due file ignorando gli spazi:

`diff -w {{vecchio_file}} {{nuovo_file}}`

- Confronta due file mostrando le differenze fianco a fianco:

`diff -y {{vecchio_file}} {{nuovo_file}}`

- Confronta due file, mostrando le differenze in formato unificato (come `git diff`):

`diff -u {{vecchio_file}} {{nuovo_file}}`

- Confronta due cartelle ricorsivamente (mostra i nomi dei file/cartella diversi e le differenze trai file):

`diff -r {{old_cartella}} {{new_cartella}}`

- Confronta due cartelle mostrando solamente il nome dei file diversi:

`diff -rq {{old_cartella}} {{new_cartella}}`
