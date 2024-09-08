# plasmashell

> Start and restart Plasma Desktop.
> More information: <https://invent.kde.org/plasma/plasma-desktop>.

- Restart `plasmashell`:

`systemctl restart --user plasma-plasmashell`

- Restart `plasmashell` without systemd:

`plasmashell --replace & disown`

- Display [h]elp on command-line options:

`plasmashell --help`

- Display help, including Qt options:

`plasmashell --help-all`
