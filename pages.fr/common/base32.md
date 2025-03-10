# base32

> Encode ou décode un fichier ou l'entrée standard vers ou depuis la base 32, et retourne le résultat à la sortie standard.
> Plus d'informations : <https://manned.org/base32>.

- Encode un fichier :

`base32 {{chemin/vers/fichier}}`

- Envelopper la sortie codée à une largeur spécifique (`0` désactive l'enveloppement) :

`base32 {{[-w|--wrap]}} {{0|76|...}} {{chemin/vers/fichier}}`

- Décode un fichier :

`base32 {{[-d|--decode]}} {{chemin/vers/fichier}}`

- Encode depuis `stdin` :

`{{commande}} | base32`

- Décode depuis `stdin` :

`{{commande}} | base32 {{[-d|--decode]}}`
