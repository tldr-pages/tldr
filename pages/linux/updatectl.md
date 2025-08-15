# updatectl

> System update utility.
> More information: <https://www.freedesktop.org/software/systemd/man/updatectl.html>.

- Apply an update:

`updatectl update {{target}}`

- Apply update and then reboot system:

`updatectl --reboot update {{target}}`

- Show data about the target and its versions:

`updatectl list {{target}}`

- Return local data about a target without fetching from the network:

`updatectl --offline list {{target}}`

- Suppress data headers for returned information:

`updatectl --no-legend list {{target}}`

- Check to see if a target has any available updates:

`updatectl check {{target}}`

- Clean up old versions of a specified target:

`updatectl vacuum {{target}}`

- Display help:

`updatectl {{[-h|--help]}}`
