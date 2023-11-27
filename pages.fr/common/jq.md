# jq

> Un processeur JSON en ligne de commande qui utilise un langage dédié (DSL).
> Plus d'informations : <https://stedolan.github.io/jq/manual/>.

- Exécute une expression spécifique (affiche une sortie JSON coloré et formaté) :

`{{cat chemin/vers/fichier.json}} | jq '.'`

- Exécute un script spécifique :

`{{cat chemin/vers/fichier.json}} | jq --from-file {{chemin/vers/script.jq}}`

- Transmet des arguments spécifiques :

`{{cat chemin/vers/fichier.json}} | jq {{--arg "nom1" "valeur1" --arg "nom2" "valeur2" ...}} '{{. + $ARGS.named}}'`

- Imprime des clés spécifiques :

`{{cat chemin/vers/fichier.json}} | jq '{{.clé1, .clé2, ...}}'`

- Imprime des éléments spécifiques du tableau :

`{{cat chemin/vers/fichier.json}} | jq '{{.[index1], .[index2], ...}}'`

- Imprime tous les éléments du tableau/les clés de l'objet :

`{{cat chemin/vers/fichier.json}} | jq '.[]'`

- Ajoute/supprime des clés spécifiques :

`{{cat chemin/vers/fichier.json}} | jq '. {{+|-}} {{{"clé1": "valeur1", "clé2": "valeur2", ...}}}'`
