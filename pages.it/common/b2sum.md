# b2sum

> Calcola checksum crittografici BLAKE2.
> Maggiori informazioni: <https://www.gnu.org/software/coreutils/manual/html_node/b2sum-invocation.html>.

- Calcola il checksum BLAKE2 per uno o più file:

`b2sum {{percorso/del/file1 percorso/del/file2 ...}}`

- Calcola e salva l'elenco dei checksum BLAKE2 in un file:

`b2sum {{percorso/del/file1 percorso/del/file2 ...}} > {{percorso/del/file}}.b2`

- Calcola un checksum BLAKE2 da `stdin`:

`{{comando}} | b2sum`

- Legge un file di checksum BLAKE2 e nomi di file e verifica che tutti i file abbiano checksum corrispondenti:

`b2sum {{[-c|--check]}} {{percorso/del/file}}.b2`

- Mostra un messaggio solo per file mancanti o quando la verifica fallisce:

`b2sum {{[-c|--check]}} --quiet {{percorso/del/file}}.b2`

- Mostra un messaggio solo quando la verifica fallisce, ignorando i file mancanti:

`b2sum --ignore-missing {{[-c|--check]}} --quiet {{percorso/del/file}}.b2`

- Verifica un checksum BLAKE2 noto di un file:

`echo {{checksum_blake2_conosciuto_del_file}} {{percorso/del/file}} | b2sum {{[-c|--check]}}`
