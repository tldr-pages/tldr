# base64

> Encode ou décode un fichier ou l'entrée standard vers ou depuis la base 64, et retourne le résultat à la sortie standard.
> Plus d'informations : <https://manned.org/base64>.

- Encode un fichier :

`base64 {{chemin/vers/fichier}}`

- Envelopper la sortie codée à une largeur spécifique (`0` désactive l'enveloppement) :

`base64 {{[-w|--wrap]}} {{0|76|...}} {{chemin/vers/fichier}}`

- Décode un fichier :

`base64 {{[-d|--decode]}} {{chemin/vers/fichier}}`

- Encode depuis `stdin` :

`{{commande}} | base64`

- Décode depuis `stdin` :

`{{commande}} | base64 {{[-d|--decode]}}`
