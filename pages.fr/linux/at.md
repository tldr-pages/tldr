# at

> Planifie l'exécution d'une commande une fois à un moment donné.
> Plus d'information : <https://www.man7.org/linux/man-pages/man1/at.1p.html>.

- Ouvre un prompt `at` pour créer un ensemble de commandes plannifiées, appuyer sur `Ctrl + D` pour sauvergarder et quitter :

`at {{hh:mm}}`

- Exécute la commande et envoie un courriel du résultat en utilisant un programme local de courriels tel que sendmail :

`at {{hh:mm}} -m`

- Exécute un script à une heure donnée :

`at {{hh:mm}} -f {{chemin/vers/fichier}}`

- Affiche une notification système le 18 Février à 23h :

`echo "notify-send '{{On se réveille!}}'" | at {{11pm}} {{Feb 18}}`
