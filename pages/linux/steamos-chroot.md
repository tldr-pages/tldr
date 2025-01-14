# steamos-chroot

> Switch root directory in a SteamOS environment.
> More information: <https://gitlab.com/users/evlaV/projects>.

- Switch to the other A/B partition:

`steamos-chroot --partset other`

- Switch to a partition on another drive:

`steamos-chroot --disk {{/dev/sdX}} --partset {{A|B}}`

- Display help:

`steamos-chroot --help`
