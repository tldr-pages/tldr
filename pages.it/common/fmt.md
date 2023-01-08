# fmt

> Riformatta i paragrafi di un file di testo unendoli e limitando la larghezza delle righe a un dato numero di caratteri (di default 75).
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/fmt>.

- Riformatta un file:

`fmt {{percorso/del/file}}`

- Riformatta un file producendo linee di (al massimo) `n` caratteri:

`fmt -w {{n}} {{percorso/del/file}}`

- Riformatta un file senza unire assieme le linee più corte della data larghezza:

`fmt -s {{percorso/del/file}}`

- Riformatta un file usando una spaziatura uniforme (1 spazio tra due parole e 2 spazi tra due paragrafi):

`fmt -u {{percorso/del/file}}`
