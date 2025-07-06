# gdm

> The GNOME Display Manager (GDM) is a replacement for the X Display Manager (XDM).
> See also: `gdm-binary`, `gdmsetup`, `gdm-stop`, `gdm-restart`, `gdm-safe-restart`.
> More information: <https://manned.org/gdm>.

- Run the GNOME Display Manager application:

`gdm`

- Prevent `gdm` from being run as a daemon background process:

`gdm --nodaemon`

- Disable `gdm` management of local console X servers for headless or remote environments:

`gdm --no-console`

- Prevent sanitizing environment variables that start with `LD_`:

`gdm --preserve-ld-vars`

- Display help:

`gdm --help`

- Display version:

`gdm --version`
