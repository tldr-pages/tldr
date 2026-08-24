# age

> Un outil de chiffrement de fichiers simple, moderne et sécurisé.
> Voir aussi : `age-keygen`, `age-inspect`.
> Plus d'informations : <https://github.com/FiloSottile/age#usage>.

- Génère un fichier chiffré déchiffrable avec une phrase de passe :

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{chemin/vers/fichier_chiffré.age}} {{chemin/vers/fichier_non_chiffré}}`

- Chiffre un fichier avec une ou plusieurs clés publiques entrées comme des littéraux (répéter `--recipient` pour plusieurs clés) :

`age {{[-r|--recipient]}} {{clé_publique}} {{[-o|--output]}} {{chemin/vers/fichier_chiffré.age}} {{chemin/vers/fichier_non_chiffré}}`

- Chiffre un fichier avec les clés publiques spécifiées dans un fichier de destinataires (une par ligne) :

`age {{[-R|--recipients-file]}} {{chemin/vers/fichier_destinataires.txt}} {{[-o|--output]}} {{chemin/vers/fichier_chiffré.age}} {{chemin/vers/fichier_non_chiffré}}`

- Déchiffre un fichier avec une phrase de passe :

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{chemin/vers/fichier_déchiffré}} {{chemin/vers/fichier_chiffré.age}}`

- Déchiffre un fichier avec un fichier de clé privée :

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{chemin/vers/fichier_clé_privée}} {{[-o|--output]}} {{chemin/vers/fichier_déchiffré}} {{chemin/vers/fichier_chiffré.age}}`
