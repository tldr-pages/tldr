# wirepumbler

> A modular session/policy manager for PipeWire and a GObject-based high-level library that wraps PipeWire’s API.
> See also: `wpctl`, `pipewire`.
> More information: <https://pipewire.pages.freedesktop.org/wireplumber/running-wireplumber-daemon.html>.

- Make WirePumbler start with the user session, starting it immediately (for `systemd` systems):

`systemctl --user --now enable wireplumber`

- Run wirepumbler, after `pipewire` is started (recommended for non-`systemd` systems):

`wirepumbler`

- Specify a different context config file:

`wirepumbler --config-file {{path/to/file}}`

- Display help:

`wirepumbler --help`

- Display version:

`wirepumbler --version`
