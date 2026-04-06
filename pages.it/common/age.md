# age

> Strumento semplice, moderno e sicuro per la crittografia di file.
> Vedi anche: `age-keygen`.
> Maggiori informazioni: <https://github.com/FiloSottile/age#usage>.

- Crea un file crittografato che può essere decrittato con una passphrase:

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{percorso/file_crittografato.age}} {{percorso/file_non_crittografato}}`

- Crittografa un file con una o più chiavi pubbliche inserite come literali (ripeti il flag `--recipient` per specificare più chiavi pubbliche):

`age {{[-r|--recipient]}} {{chiave_pubblica}} {{[-o|--output]}} {{percorso/file_crittografato.age}} {{percorso/file_non_crittografato}}`

- Crittografa un file per uno o più destinatari con le loro chiavi pubbliche specificate in un file (una per riga):

`age {{[-R|--recipients-file]}} {{percorso/file_destinatari.txt}} {{[-o|--output]}} {{percorso/file_crittografato.age}} {{percorso/file_non_crittografato}}`

- Decrittografa un file con una passphrase:

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{percorso/file_decrittografato}} {{percorso/file_crittografato.age}}`

- Decrittografa un file con un file di chiave privata:

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{percorso/file_chiave_privata}} {{[-o|--output]}} {{percorso/file_decrittografato}} {{percorso/file_crittografato.age}}`
