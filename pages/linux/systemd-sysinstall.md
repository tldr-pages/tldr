# systemd-sysinstall

> A simple operating system installer.
> Meant to run interactively when booting from installation media, but can also be started from a shell.
> See also: `systemd-repart`, `systemd-firstboot`, `systemd-creds`, `bootctl`.
> More information: <https://www.freedesktop.org/software/systemd/man/latest/systemd-sysinstall.html>.

- Start the interactive installer and choose the target disk when prompted:

`sudo systemd-sysinstall`

- Install to a specific disk:

`sudo systemd-sysinstall {{/dev/sdX}}`

- Erase the target disk and install without asking for confirmation:

`sudo systemd-sysinstall --erase yes --confirm no {{/dev/sdX}}`

- Register the boot loader in the firmware boot menu:

`sudo systemd-sysinstall --variables yes {{/dev/sdX}}`

- Install a specific unified kernel image (UKI) instead of the currently booted one:

`sudo systemd-sysinstall --kernel {{path/to/kernel.efi}} {{/dev/sdX}}`

- Pass the root user's SSH authorized keys to the installed system:

`sudo systemd-sysinstall --load-credential ssh.authorized_keys.root:{{path/to/file}} {{/dev/sdX}}`

- Display help:

`systemd-sysinstall {{[-h|--help]}}`

- Display version:

`systemd-sysinstall --version`
