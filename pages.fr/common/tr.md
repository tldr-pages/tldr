# tr

> Convertisseur de caractères : exécute des remplacements basés sur des caractères uniques et des jeux de caractères.
> Plus d'informations : <https://www.gnu.org/software/coreutils/manual/html_node/tr-invocation.html>.

- Remplace toutes les occurrences d'un caractère dans un fichier, et affiche le résultat :

`tr <{{chemin/vers/fichier}} {{caractère_recherché}} {{caractère_remplacé}}`

- Remplace toutes les occurrences d'un caractère dans la sortie d'une autre commande :

`echo {{texte}} | tr {{caractère_recherché}} {{caractère_remplacé}}`

- Fais correspondre chaque caractère du premier ensemble au caractère correspondant du second ensemble :

`tr <{{chemin/vers/fichier}} '{{abcd}}' '{{jkmn}}'`

- Supprime toutes les occurrences de l'ensemble de caractères spécifié dans l'entrée :

`tr <{{chemin/vers/fichier}} {{[-d|--delete]}} '{{caractères_en_entrée}}'`

- Comprime une série de caractères identiques en un seul caractère :

`tr <{{chemin/vers/fichier}} {{[-s|--squeeze-repeats]}} '{{caractères_en_entrée}}'`

- Traduis le contenu d'un fichier en majuscules :

`tr <{{chemin/vers/fichier}} "[:lower:]" "[:upper:]"`

- Supprime les caractères non imprimables d'un fichier :

`tr <{{chemin/vers/fichier}} {{[-cd|--complement --delete]}} "[:print:]"`
