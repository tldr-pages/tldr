# age

> Strumento semplice, moderno e sicuro per la crittografia di file.
> Vedi anche: `age-keygen`.
> Maggiori informazioni: <https://github.com/FiloSottile/age#usage>.

- Crea un file crittografato decifrabile con passphrase:

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{percorso/al/file_crittografato.age}} {{percorso/al/file_non_crittografato}}`

- Crittografa un file con una o più chiavi pubbliche come literali (ripeti `--recipient` per più chiavi):

`age {{[-r|--recipient]}} {{chiave_pubblica}} {{[-o|--output]}} {{percorso/al/file_crittografato.age}} {{percorso/al/file_non_crittografato}}`

- Crittografa un file per destinatari con chiavi pubbliche da file (una per riga):

`age {{[-R|--recipients-file]}} {{percorso/al/file_destinatari.txt}} {{[-o|--output]}} {{percorso/al/file_crittografato.age}} {{percorso/al/file_non_crittografato}}`

- Decrittografa un file con passphrase:

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{percorso/al/file_decrittografato}} {{percorso/al/file_crittografato.age}}`

- Decrittografa un file con file chiave privata:

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{percorso/al/file_chiave_privata}} {{[-o|--output]}} {{percorso/al/file_decrittografato}} {{percorso/al/file_crittografato.age}}`
