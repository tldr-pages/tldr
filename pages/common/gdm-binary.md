# gdm-binary

> The GNOME Display Manager (GDM) is a replacement for the X Display Manager (XDM).
> See also: `gdm`, `gdmsetup`, `gdm-stop`, `gdm-restart`, `gdm-safe-restart`.
> More information: <https://manned.org/gdm>.

- Run the GNOME Display Manager application:

`gdm-binary`

- Prevent `gdm` from being run as a daemon background process:

`gdm-binary --nodaemon`

- Disable `gdm` management of local console X servers for headless or remote environments:

`gdm-binary --no-console`

- Prevent sanitizing `ENV` variables that start with `LD_`:

`gdm-binary --preserve-ld-vars`

- Show `gdm` version:

`gdm-binary --version`

- Show `gdm` help message:

`gdm-binary --help`
