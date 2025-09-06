# dunst

> A lightweight and customizable notification daemon for X11 and Wayland.
> If not started manually, D-Bus will automatically start `dunst` when a notification is sent.
> More information: <https://dunst-project.org/documentation/dunst>.

- Start `dunst`:

`dunst`

- Display a notification on startup:

`dunst -startup_notification`

- Print coming notifications to `stdout`:

`dunst -print`

- Use the specified configuration file (default: `$XDG_CONFIG_HOME/dunst/dunstrc`):

`dunst -config {{path/to/file}}`
