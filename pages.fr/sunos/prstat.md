# prstat

> Signale les statistiques de processus actifs.
> Plus d'informations : <https://www.unix.com/man-page/sunos/1m/prstat>.

- Examine tous les processus et rapporte les statistiques triées par utilisation du processeur :

`prstat`

- Examine tous les processus et rapporte les statistiques triées par utilisation de la mémoire :

`prstat -s rss`

- Rapporte le résumé de l'utilisation totale pour chaque utilisateur :

`prstat -t`

- Rapporte les informations comptables du processus de micro-état :

`prstat -m`

- Imprime une liste des 5 meilleurs processeurs utilisant des processus chaque seconde :

`prstat -c -n 5 -s cpu 1`
