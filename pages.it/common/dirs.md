# dirs

> Mostra o manipola uno stack di cartelle.
> Uno stack di cartelle è una lista di cartelle recentemente visitate che può essere manipolata con i comandi `pushd` e `popd`.
> Maggiori informazioni: <https://www.gnu.org/software/bash/manual/bash.html#Directory-Stack-Builtins>.

- Mostra lo stack di cartelle dividendo i nomi con uno spazio:

`dirs`

- Mostra lo stack di cartelle una per riga:

`dirs -p`

- Mostra solo l'ennesima directory dello stack (gli indici partono da 0):

`dirs +{{N}}`

- Pulisci lo stack di cartelle:

`dirs -c`
