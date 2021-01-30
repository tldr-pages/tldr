# vim

> Vim (Vi IMproved), un editeur de texte en ligne de commandes, fournit plusieurs modes pour differentes manipulations de texte.
> Pressez `i` pour passer en mode édition. `<Esc>` revient au mode normal, qui ne permet pas l insertion de code.
> Plus d'informations : <https://www.vim.org>.

- Ouvrir un fichier :

`vim {{chemin/vers/fichier}}`

- consulter le manuel utilisateur :

`:help<Enter>`

- Sauvegarder et fermer :

`:wq<Enter>`

- Ouvrir un fichier a une ligne specifiée :

`vim +{{numero_ligne}} {{chemin/vers/fichier}}`

- Annuler la derniere operation :

`u`

- Rechercher un pattern dans un fichier (appuyez `n`/`N` pour aller a la prochaine/précedante occurence) :

`/{{pattern_recherche}}<Enter>`

- Effectuer une substition par éxpression reguliere dans tout le fichier :

`:%s/{{pattern}}/{{replacement}}/g<Enter>`

- Afficher les numeros de ligne :

`:set nu<Enter>`
