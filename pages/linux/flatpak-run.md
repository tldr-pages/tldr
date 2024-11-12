# flatpak run

> Run flatpak applications and runtimes.
> More information: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak-run>.

- Run an installed application:

`flatpak run {{com.example.app}}`

- Run an installed application from a specific branch e.g. stable, beta, master:

`flatpak run --branch={{stable|beta|master|...}} {{com.example.app}}`

- Run an interactive shell inside a flatpak:

`flatpak run --command={{sh}} {{com.example.app}}`
