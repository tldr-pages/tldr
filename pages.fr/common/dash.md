# dash

> Debian Almquist SHell, une implémentation de `sh` moderne, conforme à POSIX (non compatible avec Bash).
> Plus d'informations : <https://manned.org/dash>.

- Démarrer une session shell interactive :

`dash`

- Exécuter une commande, puis terminer la session :

`dash -c "{{commande}}"`

- Exécuter un script :

`dash {{chemin/vers/le/script.sh}}`

- Exécuter un script en affichant chaque commande avant de l'exécuter :

`dash -x {{chemin/vers/le/script.sh}}`

- Exécuter un script en s'arrêtant à la première erreur :

`dash -e {{chemin/vers/le/script.sh}}`

- Lire et exécuter des commandes depuis l'entrée standard `stdin` :

`dash -s`
