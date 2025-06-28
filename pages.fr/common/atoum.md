# atoum

> Un framework de test unitaire pour PHP simple, moderne et intuitif.
> Plus d'informations : <https://atoum.readthedocs.io/en/latest/option_cli.html>.

- Initialise un fichier de configuration :

`atoum --init`

- Lance les tests :

`atoum`

- Lance les tests avec un fichier de configuration donné :

`atoum {{[-c|--configuration]}} {{chemin/vers/fichier}}`

- Lance un fichier de test spécifique :

`atoum {{[-f|--files]}} {{chemin/vers/fichier}}`

- Lance les tests présent dans dossier donné :

`atoum {{[-d|--directories]}} {{chemin/vers/dossier}}`

- Lance tous les tests sous un certain namespace :

`atoum {{[-ns|--namespaces]}} {{namespace}}`

- Lance tous les tests avec un certain tag :

`atoum {{[-t|--tags]}} {{tag}}`

- Charge un fichier d'amorce avant de lancer les tests :

`atoum {{[-bf|--bootstrap-file]}} {{chemin/vers/fichier}}`
