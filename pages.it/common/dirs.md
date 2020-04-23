# dirs

> Mostra o manipola uno stack di directory.
> Uno stack di directory è una lista di directory recentemente visitate che può essere manipolata con i comandi `pushd` e `popd`.

- Mostra lo stack di directory dividendo i nomi con uno spazio:

`dirs`

- Mostra lo stack di directory una per riga:

`dirs -p`

- Mostra solo l'ennesima directory dello stack (gli indici partono da 0):

`dirs +{{N}}`

- Pulisci lo stack di directory:

`dirs -c`
