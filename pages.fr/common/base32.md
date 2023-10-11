# base32

> Encode ou décode un fichier ou l'entrée standard vers ou depuis la base 32, et retourne le résultat à la sortie standard.
> Plus d'informations : <https://www.gnu.org/software/coreutils/base32>.

- Encode un fichier :

`base32 {{fichier}}`

- Décode un fichier :

`base32 --decode {{fichier}}`

- Encode depuis `stdin` :

`{{commande}} | base32`

- Décode depuis `stdin` :

`{{commande}} | base32 --decode`
