# as

> Assembler GNU portabile.
> Progettato principalmente per assemblare l'output di `gcc` ed utilizzarlo con `ld`.
> Maggiori informazioni: <https://www.unix.com/man-page/osx/1/as/>.

- Assembla un file, scrivendo l'output su a.out:

`as {{file.s}}`

- Assembla l'output nel file dato:

`as {{file.s}} -o {{out.o}}`

- Genera l'output più velocemente saltando gli spazi e senza preprocessare i commenti. (Questo comando dovrebbe essere utilizzato solo con compilatori fidati):

`as -f {{file.s}}`

- Includi un percorso dato alla lista delle directory in cui cercare i file specificati nelle direttive `.include`:

`as -I {{path/to/directory}} {{file.s}}`
