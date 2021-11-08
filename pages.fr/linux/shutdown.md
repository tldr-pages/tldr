# shutdown

> Éteint et redémarre le système.
> Plus d'informations : <https://manned.org/shutdown.8>.

- Éteint (arrête) immédiatement :

`shutdown -h now`

- Redémarre immédiatement :

`shutdown -r now`

- Redémarre dans 5 minutes :

`shutdown -r +{{5}} &`

- Éteint à 1:00 pm (Utilise un format 24h) :

`shutdown -h 13:00`

- Annule une opération d'arrêt ou de redémarrage du système en attente :

`shutdown -c`
