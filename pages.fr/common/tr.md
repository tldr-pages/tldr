# tr

> Convertisseur de caractères : exécute des remplacements basés sur des caractères uniques et des jeux de caractères.
> Plus d'informations : <https://www.gnu.org/software/coreutils/tr>.

- Remplace toutes les occurrences d'un caractère dans un fichier, et affiche le résultat :

`tr {{caractère_recherché}} {{caractère_remplacé}} < {{fichier}}`

- Remplace toutes les occurrences d'un caractère dans la sortie d'une autre commande :

`echo {{texte}} | tr {{caractère_recherché}} {{caractère_remplacé}}`

- Fais correspondre chaque caractère du premier ensemble au caractère correspondant du second ensemble :

`tr '{{abcd}}' '{{jkmn}}' < {{fichier}}`

- Supprime toutes les occurrences de l'ensemble de caractères spécifié dans l'entrée :

`tr -d '{{caractères_en_entrée}}' < {{fichier}}`

- Comprime une série de caractères identiques en un seul caractère :

`tr -s '{{caractères_en_entrée}}' < {{fichier}}`

- Traduis le contenu d'un fichier en majuscules :

`tr "[:lower:]" "[:upper:]" < {{fichier}}`

- Supprime les caractères non imprimables d'un fichier :

`tr -cd "[:print:]" < {{fichier}}`
