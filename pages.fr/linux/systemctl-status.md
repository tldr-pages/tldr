# systemctl status

> Affiche l’état des unités systemd.
> Plus d'informations : <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#status%20PATTERN%E2%80%A6%7CPID%E2%80%A6%5D>.

- Affiche l’état d’une unité systemd :

`systemctl status {{unité}}.{{service|timer|socket|target|...}}`

- Affiche l’état des unités ayant échoué :

`systemctl status --failed`

- Liste tous les services en cours d’exécution :

`systemctl status`

- Liste toutes les unités du système :

`systemctl status {{[-a|--all]}}`

- Liste toutes les unités d’un type spécifique :

`systemctl status {{[-t|--type]}} {{service|timer|socket|target|...}}`

- Liste toutes les unités ayant un état spécifique :

`systemctl status --state {{active|inactive|failed}}`

- Affiche l’état d’une unité utilisateur :

`systemctl status {{unité}} --user`
