# plasmashell

> Start and restart Plasma Desktop.
> More information: <https://invent.kde.org/plasma/plasma-desktop>.

- Restart `plasmashell`:

`systemctl restart --user plasma-plasmashell`

- Restart `plasmashell` without systemd:

`plasmashell --replace & disown`
