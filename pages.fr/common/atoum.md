# atoum

> Un framework de test unitaire pour PHP simple, moderne et intuitif.
> Plus d'informations : <http://atoum.org>.

- Initialise un fichier de configuration :

`atoum --init`

- Lance les tests :

`atoum`

- Lance les tests avec un fichier de configuration donné :

`atoum -c {{chemin/vers/fichier}}`

- Lance un fichier de test spécifique :

`atoum -f {{chemin/vers/fichier}}`

- Lance les tests présent dans dossier donné :

`atoum -d {{chemin/vers/dossier}}`

- Lance tous les tests sous un certain namespace :

`atoum -ns {{namespace}}`

- Lance tous les tests avec un certain tag :

`atoum -t {{tag}}`

- Charge un fichier d'amorce avant de lancer les tests :

`atoum --bootstrap-file {{chemin/vers/fichier}}`
