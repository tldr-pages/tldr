# enca

> Rileva e converti l'encoding di file di testo.
> Maggiori informazioni: <https://github.com/nijel/enca>.

- Rileva l'encoding di uno o più file in base alla locale di sistema:

`enca {{file1 file2 ...}}`

- Rileva l'encoding specificando un linguaggio nel formato di locale POSIX/C (e.g. zh_CN, en_US):

`enca -L {{linguaggio}} {{file1 file2 ...}}`

- Converti file ad uno specifico encoding:

`enca -L {{linguaggio}} -x {{encoding}} {{file1 file2 ...}}`

- Crea una copia di un file esistente utilizzando un encoding diverso:

`enca -L {{linguaggio}} -x {{encoding_finale}} < {{file_originale}} > {{nuovo_file}}`
