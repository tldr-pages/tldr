# lrzuntar

> Un ambalaj pentru `lrunzip `pentru a simplifica decompresia directoarelor.
> A se vedea, de asemenea: `lrztar`, `lrzip `.

- Decomprima dintr-un fișier în directorul curent:

`lrzuntar {{path/to/archive.tar.lrz}}`

- Decomprima dintr-un fișier în directorul curent folosind un anumit număr de fire de procesor:

`lrzuntar -p {{8}} {{path/to/archive.tar.lrz}}`

- Decomprima dintr-un fișier în directorul curent și suprascrie în tăcere elementele care există deja:

`lrzuntar -f {{archive.tar.lrz}}`

- Specificați calea de ieșire:

`lrzuntar -O {{path/to/directory}} {{archive.tar.lrz}}`

- Ștergeți fișierul comprimat după decompresie:

`lrzuntar -D {{path/to/archive.tar.lrz}}`
