# udiskie

> Automounter for removable media using udisks2.
> Supports manual mounting, notifications, and tray icon.
> More information: <https://github.com/coldfix/udiskie>.

- Start udiskie with tray icon and notifications:

`udiskie --tray --notify`

- Mount all available devices:

`udiskie --mount`

- Unmount all mounted devices:

`udiskie --umount`

- Run udiskie without using a config file:

`udiskie --no-config`

- Specify a custom config file:

`udiskie --config {{path/to/config.yml}}`

- Use a custom password prompt command:

`udiskie --password-prompt '{{command}}'`

- Enable verbose output:

`udiskie --verbose`

- Suppress all output:

`udiskie --quiet`

- Show help message:

`udiskie --help`

- Show version information:

`udiskie --version`
