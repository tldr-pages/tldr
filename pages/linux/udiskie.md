# udiskie

> Automounter for removable media using udisks2.
> More information: <https://github.com/coldfix/udiskie>.

- Start udiskie with tray icon and notifications:

`udiskie --tray --notify`

- Mount all available devices:

`udiskie --mount`

- Run udiskie without using a config file:

`udiskie --no-config`

- Specify a custom config file:

`udiskie --config {{path/to/config.yml}}`

- Use a custom password prompt command:

`udiskie --password-prompt '{{command}}'`

- Enable verbose output:

`udiskie --verbose`

- Display help:

`udiskie --help`

- Display version:

`udiskie --version`
