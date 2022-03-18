# ack

> Un outil de recherche comme grep, optimisé pour les développeurs.
> Regardez aussi : `rg`, qui est beaucoup plus rapide.
> Plus d'informations : <https://beyondgrep.com/documentation>.

- Recherche des fichiers contenant une chaine de caractère ou une expression régulière dans le répertoire courant récursivement :

`ack "{{motif_de_recherche}}"`

- Recherche pour un motif insensible à la casse :

`ack --ignore-case "{{motif_de_recherche}}"`

- Recherche les lignes qui correspondent à un motif, affiche uniquement les textes correspondants et pas le reste de la ligne :

`ack -o "{{motif_de_recherche}}"`

- Limite la recherche aux fichiers d'un certain type :

`ack --type={{ruby}} "{{motif_de_recherche}}"`

- Exlcus un certain type de fichier de la recherche :

`ack --type=no{{ruby}} "{{motif_de_recherche}}"`

- Compte le nombre total de correspondances :

`ack --count --no-filename "{{motif_de_recherche}}"`

- Affiche les noms et le nombre total de correspondances pour chaque fichiers :

`ack --count --files-with-matches "{{motif_de_recherche}}"`

- Affiche toutes les valeurs qui peuvent être utilisées avec `--type` :

`ack --help-types`
