# flatpak override

> Override the runtime permissions of Flatpak applications.
> Note: Without `--user`, the default system-wide installation is changed. Without an application, the override applies to all applications.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-override>.

- Show the overrides of an application:

`flatpak override --show {{com.example.app}}`

- Grant an application access to a filesystem location:

`flatpak override --filesystem {{home|host|xdg-download|path/to/directory}} {{com.example.app}}`

- Grant an application read-only access to a directory:

`flatpak override --filesystem {{path/to/directory}}:ro {{com.example.app}}`

- Stop sharing the network with an application:

`flatpak override --unshare network {{com.example.app}}`

- Set an environment variable for an application:

`flatpak override --env {{VAR}}={{value}} {{com.example.app}}`

- Apply an override for the current user only:

`flatpak override {{[-u|--user]}} --nosocket {{wayland}} {{com.example.app}}`

- Remove all overrides of an application:

`flatpak override --reset {{com.example.app}}`
