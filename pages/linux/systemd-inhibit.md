# systemd-inhibit

> Prohibit system from entering certain power states
> Inhibitor locks may be used to block or delay system sleep and shutdown requests as well as automatic idle handling.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-inhibit.html>.

- Lists all active inhibition locks instead of acquiring one:

`systemd-inhibit --list`

- Block system shutdown with sleep command:

`systemd-inhibit --who $USER --what shutdown sleep {{5}}`

- Keep system from sleeping or idling until after download is finished:

`systemd-inhibit --what sleep:idle wget {{https://example.com/file}}`

- Ignore lid close switch until script exits:

`systemd-inhibit --what sleep:handle-lid-switch {{path/to/script}}`

- Ignore power button press while command is running:

`systemd-inhibit --what handle-power-key {{command}}`
