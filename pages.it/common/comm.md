# comm

> Seleziona o ignora linee comuni a due file. Entrambi i file devono essere ordinati.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/comm-invocation.html>.

- Produci tre colonne separate da tab: linee solo nel primo file, linee solo nel secondo file, e linee comuni ad entrambi:

`comm {{file1}} {{file2}}`

- Stampa solo le linee comune ad entrambi i file:

`comm -12 {{file1}} {{file2}}`

- Stampa solo le lin comuni ad entrambi i file, leggendone uno da standard input:

`cat {{file1}} | comm -12 - {{file2}}`

- Filtra le linee trovate solo nel primo file, salvando il risultato in un terzo file:

`comm -23 {{file1}} {{file2}} > {{file3}}`

- Filtra le linee trovate solo nel secondo file, con due file che non sono ordinati:

`comm -13 <(sort {{file1}}) <(sort {{file2}})`
