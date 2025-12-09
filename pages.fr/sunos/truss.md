# truss

> Outil de dépannage pour tracer les appels système.
> Équivalent SunOS de strace.
> Plus d'informations : <https://www.unix.com/man-page/linux/1/truss>.

- Commencez à tracer un programme en l'exécutant, en suivant tous les processus enfants :

`truss -f {{programme}}`

- Commencez à tracer un processus spécifique par son PID :

`truss -p {{pid}}`

- Commencez à tracer un programme en l'exécutant, en affichant les arguments et les variables d'environnement :

`truss -a -e {{programme}}`

- Comptez le temps, les appels et les erreurs pour chaque appel système et rapportez un résumé à la sortie du programme :

`truss -c -p {{pid}}`

- Tracez une sortie de filtrage de processus par appel système :

`truss -p {{pid}} -t {{nom_d'appel_système}}`
