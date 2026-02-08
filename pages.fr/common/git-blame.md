# git blame

> Affiche le hash de commit et le dernier auteur de chaque ligne d'un fichier.
> Plus d'informations : <https://git-scm.com/docs/git-blame>.

- Affiche le hash de commit et le nom de l'auteur en face de chaque ligne :

`git blame {{chemin/vers/fichier}}`

- Affiche le hash de commit, le nom et l'email de l'auteur en face de chaque ligne :

`git blame {{[-e|--show-email]}} {{chemin/vers/fichier}}`

- Affiche le hash de commit et le nom de l'auteur en face de chaque ligne à un commit spécifique :

`git blame {{commit}} {{chemin/vers/fichier}}`

- Affiche le hash de commit et le nom de l'auteur en face de chaque ligne avant un commit spécifique :

`git blame {{commit}}~ {{chemin/vers/fichier}}`

- Affiche le hash de commit et le nom de l'auteur en face de chaque ligne à partir d'une ligne donnée :

`git blame -L {{123}} {{chemin/vers/fichier}}`

- Annote une plage de lignes spécifique d'un fichier :

`git blame -L {{ligne_debut}},{{ligne_fin}} {{chemin/vers/fichier}}`

- Annote 10 lignes d'un fichier à partir de la première ligne correspondant à un texte donné :

`git blame -L '/{{texte}}/',+10 {{chemin/vers/fichier}}`

- Annote un fichier en ignorant les espaces et les déplacements de lignes :

`git blame -w -C -C -C {{chemin/vers/fichier}}`
