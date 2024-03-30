# bash

> Bourne-Again SHell, un interpréteur de ligne de commande compatible avec `sh`.
> Voir aussi `histexpand` pour l'expansion de l'historique.
> Plus d'informations : <https://www.gnu.org/software/bash/>.

- Démarre une session shell interactive :

`bash`

- Exécute une commande, puis termine la session :

`bash -c "{{commande}}"`

- Exécute un script :

`bash {{chemin/vers/le/script.sh}}`

- Exécute un script en affichant chaque commande avant de l'exécuter :

`bash -x {{chemin/vers/le/script.sh}}`

- Exécute un script en s'arrêtant à la première erreur :

`bash -e {{chemin/vers/le/script.sh}}`

- Lit et exécute des commandes depuis l'entrée standard `stdin` :

`bash -s`

- Affiche la version de Bash (`$BASH_VERSION` ne contenant que la version, sans les informations de license):

`bash --version`
