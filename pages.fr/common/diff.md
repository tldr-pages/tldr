# diff

> Compare deux fichiers ou répertoires.
> Plus d'informations : <https://manned.org/diff>.

- Compare deux fichiers (liste les changements pour transformer `ancien_fichier` en `nouveau_fichier`) :

`diff {{ancien_fichier}} {{nouveau_fichier}}`

- Compare deux fichiers, en ignorant l'espacement :

`diff {{[-w|--ignore-all-space]}} {{ancien_fichier}} {{nouveau_fichier}}`

- Compare deux fichiers, en affichant différences côte à côte :

`diff {{[-y|--side-by-side]}} {{ancien_fichier}} {{nouveau_fichier}}`

- Compare deux fichiers, en affichant les différences dans un format unifié (comme `git diff`) :

`diff {{[-u|--unified]}} {{ancien_fichier}} {{nouveau_fichier}}`

- Compare récursivement deux répertoires directories (affiche les noms de fichiers et de répertoires divergents ainsi que les modifications de fichiers) :

`diff {{[-r|--recursive]}} {{ancien_répertoire}} {{nouveau_répertoire}}`

- Compare deux répertoires, en affichant uniquement les fichiers qui diffèrent :

`diff {{[-r|--recursive]}} {{[-q|--brief]}} {{ancien_répertoire}} {{nouveau_répertoire}}`

- Crée un fichier patch des différences entre deux fichiers texte pour Git, en traitant les fichiers inexistants comme fichiers vides :

`diff {{[-a|--text]}} {{[-u|--unified]}} {{[-N|--new-file]}} {{ancien_fichier}} {{nouveau_fichier}} > {{diff.patch}}`
