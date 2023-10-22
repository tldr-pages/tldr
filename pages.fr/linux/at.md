# at

> Exécute des commandes à des temps détermintés.
> Plus d'informations : <https://man.archlinux.org/man/at.1>.

- Ouvre une invite `at` afin de créer un nouvel ensemble de commandes programmées, presser `Ctrl + D` pour sauvegarder et quitter :

`at {{hh:mm}}`

- Exécute les commandes et envoie les résultats par mail en utilisant un programme de messagerie local comme Sendmail :

`at {{hh:mm}} -m`

- Exécute un script à un temps donné :

`at {{hh:mm}} -f {{chemin/vers/le/script}}`

- Affiche une notification système à 23 heures le 18 Février :

`echo "notify-send '{{Debout !}}'" | at {{11pm}} {{Feb 18}}`
