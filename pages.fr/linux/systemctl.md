# systemctl

> Contrôle le système systemd et le gestionnaire de services.
> Certaines sous-commandes, telles que disable, status, reboot, etc., disposent de leur propre documentation d’utilisation.
> Plus d'informations : <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html>.

- Affiche tous les services actuellement actifs :

`systemctl status`

- Liste des unités en échec :

`systemctl --failed`

- Démarre/Arrête/Redémarre/Recharge un service :

`systemctl {{start|stop|restart|reload}} {{unité}}`

- Active/désactive une unité à démarrer au démarrage :

`systemctl {{enable|disable}} {{unité}}`

- Rechargement de systemd, recherche d'unités nouvelles ou modifiées :

`systemctl daemon-reload`

- Vérifie si une unité est en cours d'exécution/activée/en échec :

`systemctl {{is-active|is-enabled|is-failed}} {{unité}}`

- Liste toutes les unités de service, de socket, et d’automontage en filtrant selon leur état (active/en échec) :

`systemctl list-units {{[-t|--type]}} {{service|socket|automount|...}} --state {{failed|running}}`

- Affiche le contenu et le chemin absolu d’un fichier d’unité ou le modifier :

`systemctl {{cat|edit}} {{unité}}`
