# systemd-home-fallback-shell

> Run a fallback shell for users managed by `systemd-homed`.
> Used when the configured login shell is missing or cannot be executed.
> More information: <https://man7.org/linux/man-pages/man8/systemd-homed.service.8.html>.

- Start a fallback shell for the current user:

`systemd-home-fallback-shell`

- Start a fallback shell for a specific user:

`systemd-home-fallback-shell {{username}}`

- Start a fallback shell using a specific home directory path:

`systemd-home-fallback-shell --home {{/home/username}}`

- Use a specific shell instead of the default:

`systemd-home-fallback-shell --shell {{/bin/bash}} {{username}}`

- Run a command inside the fallback shell instead of starting an interactive session:

`systemd-home-fallback-shell --command "{{echo Hello}}" {{username}}`

- Increase verbosity for debugging:

`systemd-home-fallback-shell --verbose {{username}}`

- Display version:

`systemd-home-fallback-shell --version`
