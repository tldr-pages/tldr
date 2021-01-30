# git describe

> Créer un nom unique et lisible pour un objet à partir d’une référence disponible.
> Plus d'informations : <https://git-scm.com/docs/git-describe>.

- Créer un nom unique pour le commit courant (le nom contient le tag le plus recent, le nombre de commits additionnel, and le hash abrégé du commit) :

`git describe`

- Créer un nom avec un hash de commit de 4 carctéres :

`git describe --abbrev={{4}}`

- Générer un nom avec le chemin complet du tag :

`git describe --all`

- Décrire un tag Git :

`git describe {{v1.0.0}}`

- Créer un nom pour le dernier commit d'une branche donnée :

`git describe {{nom_de_branche}}`
