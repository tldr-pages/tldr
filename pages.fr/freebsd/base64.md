# base64

> Encode ou décode un fichier ou `stdin` en base64, vers `stdout` ou un autre fichier.
> Plus d'informations : <https://man.freebsd.org/cgi/man.cgi?base64>.

- Encode un fichier vers `stdout` :

`base64 {{[-i|--input]}} {{chemin/vers/fichier}}`

- Encode un fichier vers le fichier de sortie spécifié :

`base64 {{[-i|--input]}} {{chemin/vers/fichier_entrée}} {{[-o|--output]}} {{chemin/vers/fichier_sortie}}`

- Retourne à la ligne la sortie encodée à une largeur spécifique (`0` désactive le retour à la ligne) :

`base64 {{[-b|--break]}} {{0|76|...}} {{chemin/vers/fichier}}`

- Décode un fichier vers `stdout` :

`base64 {{[-d|--decode]}} {{[-i|--input]}} {{chemin/vers/fichier}}`

- Encode les données provenant de `stdin` vers `stdout` :

`{{commande}} | base64`

- Décode les données provenant de `stdin` vers `stdout` :

`{{commande}} | base64 {{[-d|--decode]}}`
