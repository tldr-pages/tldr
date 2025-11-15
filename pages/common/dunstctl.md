# dunstctl

> Control the `dunst` notification daemon.
> More information: <https://dunst-project.org/documentation/dunstctl>.

- Pause/Unpause/Toggle desktop notifications:

`dunstctl set-paused {{true|false|toggle}}`

- Close all notifications:

`dunstctl close-all`

- Delete all notifications from history:

`dunstctl history-clear`

- Display the latest notification from history:

`dunstctl history-pop`

- Reload the configuration file:

`dunstctl reload`

- Display help:

`dunstctl {{[-h|--help]}}`
