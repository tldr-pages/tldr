# git describe

> Crée un nom unique et lisible pour un objet à partir d'une référence disponible.
> Plus d'informations : <https://git-scm.com/docs/git-describe>.

- Crée un nom unique pour la validation actuelle (le nom contient le tag le plus récent, le nombre de validations additionnelles, et l'empreinte abrégée de la validation) :

`git describe`

- Crée un nom avec une empreinte de validation de 4 caractères :

`git describe --abbrev={{4}}`

- Génère un nom avec le chemin complet de l'étiquette :

`git describe --all`

- Décrit une étiquette Git :

`git describe {{v1.0.0}}`

- Crée un nom pour la dernière validation d'une branche donnée :

`git describe {{nom_branche}}`
