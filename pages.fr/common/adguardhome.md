# AdGuardHome

> Un logiciel réseau pour bloquer les pubs et les traqueurs.
> Plus d'informations : <https://github.com/AdguardTeam/AdGuardHome>.

- Lance AdGuard Home :

`AdGuardHome`

- Lance AdGuard Home avec une configuration spécifique :

`AdGuardHome --config {{chemin/vers/AdGuardHome.yaml}}`

- Configure le répertoire de travail où les données seront stockées :

`AdGuardHome --work-dir {{chemin/vers/répertoire}}`

- Installe ou désinstalle AdGuard Home comme un service :

`AdGuardHome --service {{install|uninstall}}`

- Démarre le service AdGuard Home :

`AdGuardHome --service start`

- Recharge la configuration pour le service AdGuard Home :

`AdGuardHome --service reload`

- Éteint ou redémarre le service AdGuard Home :

`AdGuardHome --service {{stop|restart}}`
