# tail

> Afficher la fin d'un fichier.
> Voir aussi : `head`.
> Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/tail-invocation.html>.

- Affiche les 10 dernières lignes d'un fichier :

`tail {{chemin/vers/fichier}}`

- Affiche les 10 dernières lignes de plusieurs fichiers :

`tail {{chemin/vers/fichier1 chemin/vers/fichier2 ...}}`

- Affiche les 5 dernières lignes d'un fichier :

`tail {{[-5|--lines 5]}} {{chemin/vers/fichier}}`

- Affiche tout le contenu d'un fichier à partir d'une `ligne` spécifique :

`tail {{[-n|--lines]}} +{{ligne}} {{chemin/vers/fichier}}`

- Affiche un `nombre` spécifique d'octets à partir de la fin d'un fichier :

`tail {{[-c|--bytes]}} {{nombre}} {{chemin/vers/fichier}}`

- Affiche les dernières lignes d'un fichier et continuer à le lire jusqu'à ce que l'on appuie sur `<Ctrl c>` :

`tail {{[-f|--follow]}} {{chemin/vers/fichier}}`

- Continue à lire le fichier jusqu'à ce que l'on appuie sur `<Ctrl c>`, même si le fichier est inaccessible :

`tail {{[-F|--retry --follow]}} {{chemin/vers/fichier}}`

- Affiche les `nombre` dernières lignes d'un fichier et actualiser toutes les `secondes` secondes :

`tail {{[-n|--lines]}} {{nombre}} {{[-s|--sleep-interval]}} {{secondes}} {{[-f|--follow]}} {{chemin/vers/fichier}}`
