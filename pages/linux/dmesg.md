# dmesg

> Write the kernel messages to `stdout`.
> See also: `journalctl`.
> More information: <https://manned.org/dmesg>.

- Show kernel messages:

`sudo dmesg`

- Show kernel messages in human-readable format (equivalent of `dmesg --color --reltime` piped to a pager):

`sudo dmesg {{[-H|--human]}}`

- Show kernel error messages:

`sudo dmesg {{[-l|--level]}} err`

- Show kernel messages and keep [w]aiting for new ones (similar to `tail --follow`):

`sudo dmesg {{[-w|--follow]}}`

- Show kernel messages emitted in the last hour:

`sudo dmesg --since "1 hour ago"`

- Show kernel messages with timestamps as differences from local time:

`sudo dmesg {{[-e|--reltime]}}`

- Show kernel messages with a timestamp for each message:

`sudo dmesg {{[-T|--ctime]}}`

- Colorize output:

`sudo dmesg {{[-L|--color]}}`
