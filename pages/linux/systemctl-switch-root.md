# systemctl switch-root

> Switch to a new root filesystem and execute a new system manager.
> More information: <https://www.freedesktop.org/software/systemd/man/systemctl.html#switch-root%20ROOT%20INIT>.

- Switch to a new root filesystem and execute its default init system:

`systemctl switch-root {{path/to/new_root}}`

- Switch to a new root filesystem and run a specific init binary:

`systemctl switch-root {{path/to/new_root}} {{/sbin/init}}`

- Switch to a new root filesystem with verbose output:

`systemctl switch-root {{path/to/new_root}} --verbose`
