# at

> Planifie l'exécution d'une commande une fois à un moment donné.
> Le service atd (ou atrun) doit être actif pour l'exécution des commandes planifiées.
> Plus d'informations : <https://manned.org/at>.

- Démarre `atd` comme un service (en tâche de fond) :

`systemctl start atd`

- Planifie l'exécution de la commande donnée dans l'entrée standard dans 5 minutes (Appuyer sur `<Ctrl d>` une fois la commande inscrite) :

`at now + 5 minutes`

- Crée des commandes de manière interactive et les exécute à un moment précis :

`at {{hh:mm}}`

- Planifie l'exécution d'une commande depuis l'entrée standard (impression echo redirigée dans un tube) aujourd'hui à 10h00 :

`echo "{{commande}}" | at 1000`

- Planifie l'exécution des commandes inclues dans un [f]ichier pour mardi prochain 21h30 :

`at -f {{chemin/vers/fichier}} 9:30 PM Tue`
