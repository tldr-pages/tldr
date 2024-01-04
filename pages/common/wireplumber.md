# wireplumber

> A modular session/policy manager for PipeWire and a GObject-based high-level library that wraps PipeWire’s API.
> See also: `wpctl`, `pipewire`.
> More information: <https://pipewire.pages.freedesktop.org/wireplumber/running-wireplumber-daemon.html>.

- Make WirePlumber start with the user session immediately (for systemd systems):

`systemctl --user --now enable wireplumber`

- Run WirePlumber, after `pipewire` is started (for non-systemd systems):

`wireplumber`

- Specify a different context configuration file:

`wireplumber --config-file {{path/to/file}}`

- Display help:

`wireplumber --help`

- Display version:

`wirepumbler --version`
