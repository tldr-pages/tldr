# age

> Uno strumento semplice, moderno e sicuro per la cifratura di file.
> Maggiori informazioni: <https://github.com/FiloSottile/age>.

- Generare un file cifrato che può essere decifrato con una passphrase:

`age --passphrase --output {{percorso/del/file_cifrato}} {{percorso/del/file_non_cifrato}}`

- Generare una coppia di chiavi, salvando la chiave privata in un file non cifrato e stampando sullo `stdout` la chiave pubblica:

`age-keygen --output {{percorso/del/file}}`

- Cifrare un file con una o più chiavi pubbliche inserite come letterali:

`age --recipient {{chiave_pubblica_1}} --recipient {{chiave_pubblica_2}} {{percorso/del/file_non_cifrato}} --output {{percorso/del/file_cifrato}}`

- Cifrare un file con una o più chiavi pubbliche specificate in un file di destinatari:

`age --recipients-file {{percorso/del/file_di_destinatari}} {{percorso/del/file_non_cifrato}} --output {{percorso/del/file_cifrato}}`

- Decifrare un file con una passphrase:

`age --decrypt --output {{percorso/del/file_decifrato}} {{percorso/del/file_cifrato}}`

- Decifrare un file con il file di una chiave privata:

`age --decrypt --identity {{percorso/del/file_chiave_privata}} --output {{percorso/del/file_decifrato}} {{percorso/del/file_cifrato}}`
