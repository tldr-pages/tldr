# bash

> Bourne-Again SHell, un interpréteur de ligne de commande compatible avec `sh`.
> Voir aussi `histexpand` pour l'expansion de l'historique.
> Plus d'informations : <https://gnu.org/software/bash/>.

- Démarrer une session shell interactive :

`bash`

- Exécuter une commande, puis terminer la session :

`bash -c "{{commande}}"`

- Exécuter un script :

`bash {{chemin/vers/le/script.sh}}`

- Exécuter un script en affichant chaque commande avant de l'exécuter :

`bash -x {{chemin/vers/le/script.sh}}`

- Exécuter un script en s'arrêtant à la première erreur :

`bash -e {{chemin/vers/le/script.sh}}`

- Lire et exécuter des commandes depuis l'entrée standard `stdin` :

`bash -s`

- Afficher la version de Bash (`$BASH_VERSION` ne contenant que la version, sans les informations de license):

`bash --version`
