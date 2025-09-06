# systemd-inhibit

> Prohibit the system from entering certain power states.
> Inhibitor locks may be used to block or delay system sleep and shutdown requests as well as automatic idle handling.
> More information: <https://www.freedesktop.org/software/systemd/man/systemd-inhibit.html>.

- List all active inhibition locks and the reasons for their creation:

`systemd-inhibit --list`

- Block system shutdown for a specified number of seconds with the `sleep` command:

`systemd-inhibit --what shutdown sleep {{5}}`

- Keep the system from sleeping or idling until the download is complete:

`systemd-inhibit --what sleep:idle wget {{https://example.com/file}}`

- Ignore lid close switch until the script exits:

`systemd-inhibit --what sleep:handle-lid-switch {{path/to/script}}`

- Ignore power button press while command is running:

`systemd-inhibit --what handle-power-key {{command}}`

- Describe who and why created the inhibitor (default: the command and its arguments for `--who` and `Unknown reason` for `--why`):

`systemd-inhibit --who {{$USER}} --why {{reason}} --what {{operation}} {{command}}`
