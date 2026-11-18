# enca

> Rileva e converti l'encoding di file di testo.
> Maggiori informazioni: <https://manned.org/enca>.

- Rileva l'encoding di uno o più file in base alla locale di sistema:

`enca {{percorso/del/file1 percorso/del/file2 ...}}`

- Rileva l'encoding specificando un linguaggio nel formato di locale POSIX/C (e.g. zh_CN, en_US):

`enca {{[-L|--language]}} {{linguaggio}} {{percorso/del/file1 percorso/del/file2 ...}}`

- Converti file ad uno specifico encoding:

`enca {{[-L|--language]}} {{linguaggio}} {{[-x|--convert-to]}} {{encoding}} {{percorso/del/file1 percorso/del/file2 ...}}`

- Crea una copia di un file esistente utilizzando un encoding diverso:

`enca <{{file_originale}} {{[-L|--language]}} {{linguaggio}} {{[-x|--convert-to]}} {{encoding_finale}} >{{nuovo_file}}`
