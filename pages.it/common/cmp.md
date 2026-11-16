# cmp

> Compara due file.
> Maggiori informazioni: <https://www.gnu.org/software/diffutils/manual/diffutils.html#Invoking-cmp>.

- Trova l'indice del primo byte e della prima riga differente tra due file:

`cmp {{percorso/del/file1}} {{percorso/del/file2}}`

- Trova ogni coppia di byte differenti ed il relativo indice:

`cmp {{[-l|--verbose]}} {{percorso/del/file1}} {{percorso/del/file2}}`
