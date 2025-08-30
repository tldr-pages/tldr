# updatectl

> System update utility.
> More information: <https://www.freedesktop.org/software/systemd/man/updatectl.html>.

- Check to see if the system has any available updates:

`updatectl check`

- Update to the latest version:

`updatectl update`

- Show update targets:

`updatectl list`

- Show data about a target and its versions:

`updatectl list {{target}}`

- Return local data about a target without fetching from the network:

`updatectl --offline list {{target}}`

- Apply an update to a target and then reboot the system:

`updatectl --reboot update {{target}}`

- Clean up old versions of a specified target:

`updatectl vacuum {{target}}`

- Display help:

`updatectl {{[-h|--help]}}`
