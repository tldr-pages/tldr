# mako

> Notification daemon for Wayland compositors.
> Can be controlled with `makoctl`.
> More information: <https://manned.org/man/arch/mako.5>.

- Start the mako notification daemon:

`mako`

- Start with a custom configuration file:

`mako --config {{path/to/config}}`

- Set maximum number of visible notifications:

`mako --max-visible {{5}}`

- Set default timeout in milliseconds (0 to disable):

`mako --default-timeout {{2000}}`

- Group notifications by application name:

`mako --group-by {{app-name}}`

- Display help:

`mako --help`

- View documentation for controlling mako:

`tldr makoctl`
