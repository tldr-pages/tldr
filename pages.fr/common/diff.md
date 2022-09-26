# diff

> Compare deux fichiers ou répertoires.
> Plus d'informations : <https://man7.org/linux/man-pages/man1/diff.1.html>.

- Compare deux fichiers (liste les changements pour transformer `ancien_fichier` en `nouveau_fichier`) :

`diff {{ancien_fichier}} {{nouveau_fichier}}`

- Compare deux fichiers, en ignorant l'espacement :

`diff --ignore-all-space {{ancien_fichier}} {{nouveau_fichier}}`

- Compare deux fichiers, en affichant différences côte à côte :

`diff --side-by-side {{ancien_fichier}} {{nouveau_fichier}}`

- Compare deux fichiers, en affichant les différences dans un format unifié (comme `git diff`) :

`diff --unified {{ancien_fichier}} {{nouveau_fichier}}`

- Compare récursivement deux répertoires directories (affiche les noms de fichiers et de répertoires divergents ainsi que les modifications de fichiers) :

`diff --recursive {{ancien_répertoire}} {{nouveau_répertoire}}`

- Compare deux répertoires, en affichant uniquement les fichiers qui diffèrent :

`diff --recursive --brief {{ancien_répertoire}} {{nouveau_répertoire}}`

- Crée un fichier patch des différences entre deux fichiers texte pour Git, en traitant les fichiers inexistants comme fichiers vides :

`diff --text --unified --new-file {{ancien_fichier}} {{nouveau_fichier}} > {{diff.patch}}`
