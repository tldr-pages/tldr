# kill

> Envoie un signal à un processus, généralement pour l'interrompre.
> Tous les signaux sauf SIGKILL et SIGSTOP peuvent être interceptés par le processus pour pouvoir se terminer proprement.
> Plus d'informations: <https://manned.org/kill>.

- Termine un processus avec le signal SIGTERM (terminaison) par défaut :

`kill {{indentifiant_processus}}`

- Liste les noms des signaux disponibles (à utiliser sans leurs préfixes `SIG`) :

`kill -l`

- Termine une tâche de fond :

`kill %{{identifiant_tâche}}`

- Termine un processus avec le signal SIGHUP ("raccrocher"). Beaucoup de daemons se rafraîchissent au lieu de terminer :

`kill -{{1|HUP}} {{indentifiant_processus}}`

- Termine un processus avec le signal SIGINT ("interruption"). Généralement initié par l'utilisateur appuyant sur `Ctrl + C` :

`kill -{{2|INT}} {{indentifiant_processus}}`

- Demande au système d'exploitation de mettre fin à un processus immédiatement (sans possibilité d'intercepter le signal) :

`kill -{{9|KILL}} {{indentifiant_processus}}`

- Demande au système d'exploitation de suspendre un processus jusqu'à recevoir le signal SIGCONT ("continue") :

`kill -{{17|STOP}} {{indentifiant_processus}}`

- Envoie le signal SIGUSR1 à tous les processus dans le groupe avec l'identifiant indiqué :

`kill -{{SIGUSR1}} -{{identifiant_groupe}}`
