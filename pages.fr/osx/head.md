# head

> Affiche les premières lignes d'un fichier.
> Plus d'informations : <https://keith.github.io/xcode-man-pages/head.1.html>.

- Affiche les 10 premières lignes d'un fichier :

`head {{chemin/vers/fichier}}`

- Affiche les 5 premières lignes de plusieurs fichiers :

`head {{[-5|--lines 5]}} {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Affiche les `nombre` premières lignes d'un fichier :

`head {{[-n|--lines]}} {{nombre}} {{chemin/vers/fichier}}`

- Affiche les n premiers `octets` d'un fichier :

`head {{[-c|--bytes]}} {{octets}} {{chemin/vers/fichier}}`
