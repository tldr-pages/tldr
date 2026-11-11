# plasmashell

> Inicia y reinicia Plasma Desktop.
> Más información: <https://invent.kde.org/plasma/plasma-desktop>.

- Reinicia `plasmashell`:

`systemctl restart --user plasma-plasmashell`

- Reinicia `plasmashell` sin systemd:

`plasmashell --replace & disown`

- Muestra la ayuda:

`plasmashell {{[-h|--help]}}`

- Muestra la ayuda, incluidas las opciones de Qt:

`plasmashell --help-all`
