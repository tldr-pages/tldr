# renice

> Modifie la priorité d’ordonnancement ou la valeur de politesse des processus en cours d’exécution.
> Les valeurs de niceness vont de -20 (priorité la plus favorable au processus) à 19 (priorité la moins favorable au processus).
> Voir aussi : `nice`.
> Plus d'informations : <https://manned.org/renice.1p>.

- Augmente ou diminue la priorité d’un [p]rocessus en cours d’exécution :

`renice -n {{3}} -p {{pid}}`

- Augmente ou diminue la priorité de tous les processus appartenant à un [u]tilisateur :

`renice -n {{-4}} -u {{uid|utilisateur}}`

- Augmente ou diminue la priorité de tous les processus appartenant à un [g]roupe de processus :

`renice -n {{5}} -g {{groupe_processus}}`
