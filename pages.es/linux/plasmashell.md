# plasmashell

> Inicia y reinicia Plasma Desktop.
> Más información: <https://invent.kde.org/plasma/plasma-desktop>.

- Reinicia `plasmashell`:

`systemctl restart --user plasma-plasmashell`

- Reinicia `plasmashell` sin systemd:

`plasmashell --replace & disown`

- Muestra ayuda en las opciones de la línea de comandos:

`plasmashell {{[-h|--help]}}`

- Muestra la ayuda, incluidas las opciones de Qt:

`plasmashell --help-all`
