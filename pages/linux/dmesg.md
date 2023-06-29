# dmesg

> Write the kernel messages to `stdout`.
> More information: <https://manned.org/dmesg>.

- Show kernel messages:

`dmesg`

- Show kernel error messages:

`dmesg --level err`

- Show kernel messages and keep reading new ones, similar to `tail -f` (available in kernels 3.5.0 and newer):

`dmesg -w`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`

- Show kernel messages with a timestamp (available in kernels 3.5.0 and newer):

`dmesg -T`

- Show kernel messages in human-readable form (available in kernels 3.5.0 and newer):

`dmesg -H`

- Colorize output (available in kernels 3.5.0 and newer):

`dmesg -L`
