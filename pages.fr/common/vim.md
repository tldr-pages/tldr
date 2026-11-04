# vim

> Vim (Vi IMproved), un éditeur de texte en ligne de commandes, fournit plusieurs modes pour différentes manipulations de texte.
> Pressez `<i>` pour passer en mode édition. `<Esc>` revient au mode normal, qui ne permet pas l insertion de code.
> Voir aussi : `vimdiff`, `vimtutor`, `nvim`, `gvim`.
> Plus d'informations : <https://www.vim.org/>.

- Ouvre un fichier :

`vim {{chemin/vers/fichier}}`

- Ouvre un fichier à une ligne spécifiée :

`vim +{{numero_ligne}} {{chemin/vers/fichier}}`

- Consulte le manuel utilisateur :

`<:>help<Enter>`

- Sauvegarde et ferme :

`{{<Esc><Z><Z>|<Esc><:>x<Enter>|<Esc><:>wq<Enter>}}`

- Annule la dernière opération :

`<Esc><u>`

- Recherche un motif dans un fichier (appuyer `<n>`/`<N>` pour aller à la prochaine / précédente occurrence) :

`</>{{motif_recherché}}<Entrée>`

- Effectuer une substitution par `regex` dans tout le fichier :

`<:>%s/{{regex}}/{{remplacement}}/g<Entrée>`

- Affiche les numéros de ligne :

`<:>set nu<Entrée>`
