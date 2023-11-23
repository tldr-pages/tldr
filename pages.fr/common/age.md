# age

> Un outil de cryptage de fichiers simple, moderne et sécurisé.
> Plus d'informations : <https://github.com/FiloSottile/age>.

- Générez un fichier crypté qui peut être décrypté avec une mot de passe:

`age --passphrase --output {{chemin/vers/fichier_crypté}} {{chemin/vers/fichier_non_crypté}}`

- Générer une paire de clés, en enregistrant la clé privée dans un fichier non crypté et en imprimant la clé publique sur `stdout`:

`age-keygen --output {{chemin/vers/fichier}}`

- Cryptage d'un fichier avec une ou plusieurs clés publiques qui sont entrées comme des littéraux:

`age --recipient {{clé_publique_1}} --recipient {{clé_publique_2}} {{chemin/vers/fichier_non_crypté}} --output {{chemin/vers/fichier_crypté}}`

- Cryptez un fichier avec une ou plusieurs clés publiques spécifiées dans un fichier de destinataires:

`age --recipients-file {{chemin/vers/fichier_destinataire}} {{chemin/vers/fichier_non_crypté}} --output {{chemin/vers/fichier_crypté}}`

- Déchiffrer un fichier avec un mot de passe:

`age --decrypt --output {{chemin/vers/fichier_décrypté}} {{chemin/vers/fichier_crypté}}`

- Decrypt a file with a private key file:

`age --decrypt --identity {{chemin/vers/fichier_clé_privée}} --output {{chemin/vers/fichier_décrypté}} {{chemin/vers/fichier_crypté}}`
