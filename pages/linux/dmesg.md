# dmesg

> Write the kernel messages to `stdout`.
> More information: <https://manned.org/dmesg>.

- Show kernel messages:

`sudo dmesg`

- Show kernel error messages:

`sudo dmesg {{[-l|--level]}} err`

- Show kernel messages and keep [w]aiting for new ones, similar to `tail --follow` (available in kernels 3.5.0 and newer):

`sudo dmesg {{[-w|--follow]}}`

- Show how much physical memory is available on this system:

`sudo dmesg | grep {{[-i|--ignore-case]}} memory`

- Show kernel messages 1 page at a time:

`sudo dmesg | less`

- Show kernel messages with a timestamp (available in kernels 3.5.0 and newer):

`sudo dmesg {{[-T|--ctime]}}`

- Show kernel messages in human-readable form (available in kernels 3.5.0 and newer):

`sudo dmesg {{[-H|--human]}}`

- Colorize output (available in kernels 3.5.0 and newer):

`sudo dmesg {{[-L|--color]}}`
