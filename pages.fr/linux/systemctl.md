# systemctl

> Contrôle le système systemd et le gestionnaire de services.
> Plus d'informations : <https://www.freedesktop.org/software/systemd/man/systemctl.html>.

- Liste des unités en échec :

`systemctl --failed`

- Démarre/arrête/redémarre/recharge un service :

`systemctl {{start|stop|restart|reload}} {{unité}}`

- Affiche le statut d'une unité :

`systemctl status {{unité}}`

- Active/désactive une unité à démarrer au démarrage :

`systemctl {{enable|disable}} {{unité}}`

- Masque/démasque une unité pour empêcher l'activation et l'activation manuelle :

`systemctl {{mask|unmask}} {{unité}}`

- Rechargement de systemd, recherche d'unités nouvelles ou modifiées :

`systemctl daemon-reload`

- Vérifie si une unité est en cours de fonctionnement :

`systemctl is-active {{unité}}`

- Vérifie si une unité est activée :

`systemctl is-enabled {{unité}}`
