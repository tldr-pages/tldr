# cmp

> Compara due file.
> Maggiori informazioni: <https://www.gnu.org/software/diffutils/manual/html_node/Invoking-cmp.html>.

- Trova l'indice del primo byte e della prima riga differente tra due file:

`cmp {{file1}} {{file2}}`

- Trova ogni coppia di byte differenti ed il relativo indice:

`cmp {{[-l|--verbose]}} {{file1}} {{file2}}`
