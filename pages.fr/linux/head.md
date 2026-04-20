# head

> Afficher le début d'un fichier.
> Voir aussi : `tail`
> Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/head-invocation.html>.

- Affiche les 10 premières lignes d'un fichier :

`head {{chemin/vers/fichier}}`

- Affiche les 10 premières lignes de plusieurs fichiers :

`head {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Affiche les 5 premières lignes d'un fichier :

`head {{[-5|--lines 5]}} {{chemin/vers/fichier}}`

- Affiche un `nombre` de lignes d'un fichier :

`head {{[-n|--lines]}} {{nombre}} {{chemin/vers/fichier}}`

- Affiche un `nombre` spécifique d'octets à partir du début d'un fichier :

`head {{[-c|--bytes]}} {{nombre}} {{chemin/vers/fichier}}`

- Affiche tout le contenu d'un fichier sauf un `nombre` de lignes à la fin :

`head {{[-n|--lines]}} -{{nombre}} {{chemin/vers/fichier}}`

- Affiche tout le contenu d'un fichier sauf un `nombre` d'octets à la fin :

`head {{[-c|--bytes]}} -{{nombre}} {{chemin/vers/fichier}}`
