# git describe

> Donner à un objet un nom "human-readable" basé sur une référence disponible.
> Plus d'informations: <https://git-scm.com/docs/git-describe>.

- Crée un nom unique pour le commit courrant (le nom contient la balise annotée la plus récente, le nombre de commit supplémentaires et le hachage de commit abrégé):

`git describe`

- Crée un nom pour le hachage de commit abregé de 4 caractŕes:

`git describe --abbrev={{4}}`

- Générer un nom avec le chemin de référence du tag:

`git describe --all`

- Décrire un tag git:

`git describe {{v1.0.0}}`

- Créer un nom pour le dernier commit de la branche:

`git describe {{nom_de_branche}}`
