# tr

> Convertisseur de caractères : exécute des remplacements basés sur des caractères uniques et des jeux de caractères.
> Plus d'informations : <https://www.gnu.org/software/coreutils/tr>.

- Remplacer toutes les occurrences d'un caractère dans un fichier, et afficher le résultat :

`tr {{caractère_recherché}} {{caractère_remplacé}} < {{fichier}}`

- Remplacer toutes les occurrences d'un caractère dans la sortie d'une autre commande :

`echo {{texte}} | tr {{caractère_recherché}} {{caractère_remplacé}}`

- Faire correspondre chaque caractère du premier ensemble au caractère correspondant du second ensemble :

`tr '{{abcd}}' '{{jkmn}}' < {{fichier}}`

- Supprimer toutes les occurrences de l'ensemble de caractères spécifié dans l'entrée :

`tr -d '{{caractères_en_entrée}}' < {{fichier}}`

- Comprimer une série de caractères identiques en un seul caractère :

`tr -s '{{caractères_en_entrée}}' < {{fichier}}`

- Traduire le contenu d'un fichier en majuscules :

`tr "[:lower:]" "[:upper:]" < {{fichier}}`

- Supprime les caractères non imprimables d'un fichier :

`tr -cd "[:print:]" < {{fichier}}`
