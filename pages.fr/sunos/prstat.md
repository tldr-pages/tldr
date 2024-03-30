# prstat

> Signaler les statistiques de processus actifs.
> Plus d'informations : <https://www.unix.com/man-page/sunos/1m/prstat>.

- Examinez tous les processus et rapportez les statistiques triées par utilisation du processeur :

`prstat`

- Examinez tous les processus et rapportez les statistiques triées par utilisation de la mémoire :

`prstat -s rss`

- Rapporter le résumé de l'utilisation totale pour chaque utilisateur :

`prstat -t`

- Rapporter les informations comptables du processus de micro-état :

`prstat -m`

- Imprimez une liste des 5 meilleurs processeurs utilisant des processus chaque seconde :

`prstat -c -n {{5}} -s cpu {{1}}`
