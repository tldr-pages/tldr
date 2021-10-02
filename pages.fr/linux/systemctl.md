# systemctl

> Contrôle le système systemd et le gestionnaire de services.
> Plus d'informations : <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Liste des unités en échec :

`systemctl --failed`

- Démarrer/arrêter/redémarrer/recharger un service :

`systemctl {{start|stop|restart|reload}} {{unité}}`

- Afficher le statut d'une unité :

`systemctl status {{unité}}`

- Activer/désactiver une unité à démarrer au démarrage :

`systemctl {{enable|disable}} {{unité}}`

- Masquer/démasquer une unité pour empêcher l'activation et l'activation manuelle :

`systemctl {{mask|unmask}} {{unité}}`

- Rechargement de systemd, recherche d'unités nouvelles ou modifiées :

`systemctl daemon-reload`

- Vérifiez si une unité est en cours de fonctionnement :

`systemctl is-active {{unité}}`

- Vérifiez si une unité est activée :

`systemctl is-enabled {{unité}}`
