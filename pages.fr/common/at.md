# at

> Planifie l'exécution d'une commande une fois à un moment donné.
> Le service atd (ou atrun) doit être actif pour l'exécution des commandes plannifiées.
> Plus d'information : <https://www.man7.org/linux/man-pages/man1/at.1p.html>.

- Planifie l'exécution de la commande donnée dans l'entrée standard dans 5 minutes (Appuyer sur `Ctrl + D` une fois la commande inscrite) :

`at now + 5 minutes`

- Planifie l'exécution d'une commande depuis l'entrée standard (impression echo redirigée dans un tube) aujourd'hui à 10h00 :

`echo "{{./ma_commande.sh}}" | at 1000`

- Planifie l'exécution des commandes inclues dans un [f]ichier pour mardi prochain 21h30 :

`at -f {{chemin/vers/fichier}} 9:30 PM Tue`
