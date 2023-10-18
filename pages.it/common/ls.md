# ls

> Elenca i contenuti di una directory.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/ls>.

- Elenca i file nella directory corrente, uno per riga:

`ls -1`

- Elenca tutti i file, inclusi quelli nascosti:

`ls -a`

- Elenca tutti i file, aggiungendo `/` in coda ai nomi delle directory:

`ls -F`

- Elenca tutti i file e mostra informazioni (permessi, proprietà, dimensione e data di ultima modifica):

`ls -la`

- Elenca tutti i file e mostra informazioni con la dimensione esposta usando un formato facilmente leggibile (KiB, MiB, GiB):

`ls -lh`

- Elenca tutti i file e mostra informazioni, ordinandoli per dimensione decrescente:

`ls -lS`

- Elenca tutti i file e mostra informazioni, ordinandoli per data di ultima modifica (i più vecchi prima):

`ls -ltr`

- Elenca solo le directory:

`ls -d */`
