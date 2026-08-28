# systemctl stop

> Arrêter des unités systemd.
> Plus d'informations : <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#stop%20PATTERN%E2%80%A6>.

- Arrêter une unité :

  `systemctl stop {{unité}}`

- Arrêter un service et masquer les avertissements :

  `systemctl stop {{unité}} --no-warn`

- Arrêter une unité utilisateur :

  `systemctl stop {{unité}} --user`
