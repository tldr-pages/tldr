# tail

> Afficher la fin d'un fichier.
> Voir aussi : `head`.
> Plus d'informations : <https://keith.github.io/xcode-man-pages/tail.1.html>.

- Affiche les 8 dernières lignes d'un fichier :

`tail -n 8 {{chemin/vers/fichier}}`

- Affiche tout le contenu d'un fichier à partir d'une `ligne` spécifique :

`tail -n +{{ligne}} {{chemin/vers/fichier}}`

- Affiche un `nombre` spécifique d'octets à partir de la fin d'un fichier :

`tail -c {{nombre}} {{chemin/vers/fichier}}`

- Affiche les dernières lignes d'un fichier et continuer à le lire jusqu'à ce que l'on appuie sur `<Ctrl c>` :

`tail -f {{chemin/vers/fichier}}`

- Continue à lire le fichier jusqu'à ce que l'on appuie sur `<Ctrl c>`, même si le fichier est inaccessible :

`tail -F {{chemin/vers/fichier}}`

- Affiche les `nombre` dernières lignes d'un fichier et actualiser toutes les `secondes` secondes :

`tail -n {{nombre}} -s {{secondes}} -f {{chemin/vers/fichier}}`
