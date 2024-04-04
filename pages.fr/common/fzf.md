# fzf

> Recherche approximative en ligne de commande.
> Similaire à `sk`.
> Plus d'informations : <https://github.com/junegunn/fzf>.

- Lance `fzf` sur tous les fichiers du répertoire spécifié :

`find {{chemin/vers/répertoire}} -type f | fzf`

- Démarre `fzf` pour les processus en cours :

`ps aux | fzf`

- Sélectionne plusieurs fichiers avec `Shift + Tab` et écrit dans un fichier :

`find {{chemin/vers/répertoire}} -type f | fzf --multi > {{chemin/vers/fichier}}`

- Lance `fzf` avec une requête donnée :

`fzf --query "{{query}}"`

- Lance `fzf` sur les entrées qui commencent par core et se terminent par go, rb, ou py :

`fzf --query "^core go$ | rb$ | py$"`

- Lance `fzf` sur les entrées qui ne correspondent pas à pyc et qui correspondent exactement à travis :

`fzf --query "!pyc 'travis"`
