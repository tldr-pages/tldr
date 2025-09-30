# b2sum

> Calcola checksum BLAKE2.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- Calcola il checksum BLAKE2 per un file:

`b2sum {{file1}}`

- Calcola checksum BLAKE2 per più file:

`b2sum {{file1}} {{file2}}`

- Leggi un file di checksum BLAKE2 e nomi di file e verifica che tutti i file abbiano lo stesso checksum:

`b2sum -c {{elenco_checksum.b2}}`

- Calcola il checksum BLAKE2 da standard input:

`{{comando}} | b2sum`
