# systemctl stop

> Arrête des unités systemd.
> Plus d'informations : <https://www.freedesktop.org/software/systemd/man/latest/systemctl.html#stop%20PATTERN%E2%80%A6>.

- Arrête une unité :

`systemctl stop {{unité}}`

- Arrête un service et masque les avertissements :

`systemctl stop {{unité}} --no-warn`

- Arrête une unité utilisateur :

`systemctl stop {{unité}} --user`
