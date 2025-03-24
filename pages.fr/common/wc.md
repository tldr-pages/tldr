# wc

> Compte les lignes, les mots ou les octets.
> Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/wc-invocation.html>.

- Compte les lignes d'un fichier :

`wc {{[-l|--lines]}} {{chemin/vers/fichier}}`

- Compte les mots d'un fichier :

`wc {{[-w|--words]}} {{chemin/vers/fichier}}`

- Compte les octets d'un fichier :

`wc {{[-c|--bytes]}} {{chemin/vers/fichier}}`

- Compte les caractères d'un fichier (en prenant en compte l'ensemble des caractères multi-octets) :

`wc {{[-m|--chars]}} {{chemin/vers/fichier}}`

- Compte les lignes, les mots et les caractères depuis l'entrée standard `stdin` :

`{{find .}} | wc`

- Compte la longueur en nombre de caractères de la plus grande ligne d'un fichier :

`wc {{[-L|--max-line-length]}} {{chemin/vers/fichier}}`
