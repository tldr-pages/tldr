# rg

> Ripgrep, un outil de recherche récursive orienté ligne.
> Se veut une alternative plus rapide à `grep`.
> Plus d'informations : <https://github.com/BurntSushi/ripgrep/blob/master/GUIDE.md>.

- Rechercher de manière récursive un motif (`expression régulière`) dans le répertoire courant :

`rg {{motif}}`

- Rechercher de manière récursive un motif dans un fichier ou un répertoire :

`rg {{motif}} {{chemin/vers/fichier_ou_répertoire}}`

- Rechercher une chaîne de caractères littérale :

`rg {{[-F|--fixed-strings]}} -- {{chaîne}}`

- Inclure les fichiers cachés ainsi que les éléments listés dans `.gitignore` :

`rg {{[-.|--hidden]}} --no-ignore {{motif}}`

- Rechercher uniquement dans les fichiers correspondant au(x) motif(s) de type `glob` (par ex. `README.*` ; utilisez `!motif_de_fichier` pour exclure) :

`rg {{motif}} {{[-g|--glob]}} '{{motif_glob_de_fichier}}'`

- Lister de manière récursive les noms de fichiers dans le répertoire courant et mettre en évidence ceux qui correspondent à un motif :

`rg --files | rg {{[--passthru|--passthrough]}} {{motif}}`

- Lister uniquement les fichiers contenant une correspondance (utile lors de l'utilisation de tubes/pipes vers d'autres commandes) :

`rg {{[-l|--files-with-matches]}} {{motif}}`

- Afficher les lignes qui ne correspondent pas au motif :

`rg {{[-v|--invert-match]}} {{motif}}`
