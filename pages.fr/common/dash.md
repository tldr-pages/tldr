# dash

> Debian Almquist SHell, une implémentation de `sh` moderne, conforme à POSIX (non compatible avec Bash).
> Plus d'informations : <https://manned.org/dash>.

- Démarre une session shell interactive :

`dash`

- Exécute une commande, puis termine la session :

`dash -c "{{commande}}"`

- Exécute un script :

`dash {{chemin/vers/le/script.sh}}`

- Exécute un script en affichant chaque commande avant de l'exécuter :

`dash -x {{chemin/vers/le/script.sh}}`

- Exécute un script en s'arrêtant à la première erreur :

`dash -e {{chemin/vers/le/script.sh}}`

- Lit et exécute des commandes depuis l'entrée standard `stdin` :

`dash -s`
