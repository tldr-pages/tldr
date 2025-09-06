# reboot

> Redémarre le système.
> Plus d'informations : <https://manned.org/reboot.8>.

- Redémarre le système :

`reboot`

- Éteint le système (identique à `poweroff`) :

`reboot {{[-p|--poweroff]}}`

- Arrête (met fin à tous les processus et arrête le processeur) le système (identique à `halt`) :

`reboot --halt`

- Redémarre immédiatement sans contacter le gestionnaire du système :

`reboot {{[-f|--force]}}`

- Écrit l'entrée wtmp shutdown sans redémarrer le système :

`reboot {{[-w|--wtmp-only]}}`
