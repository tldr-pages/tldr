# wc

> Compte les lignes, les mots ou les octets.
> Plus d'informations : <https://www.gnu.org/software/coreutils/wc>.

- Compte les lignes d'un fichier :

`wc -l {{file}}`

- Compte les mots d'un fichier :

`wc -w {{file}}`

- Compte les caractères (octets) d'un fichier :

`wc -c {{file}}`

- Compte les caractères d'un fichier (en prenant en compte l'ensemble des caractères multi-octets) :

`wc -m {{file}}`

- Utilisez l'entrée standard pour compter les lignes, les mots et les caractères (octets) dans cet ordre :

`{{find .}} | wc`
