# dmesg

> Write the kernel messages to `stdout`.
> More information: <https://manned.org/dmesg>.

- Show kernel messages:

`sudo dmesg`

- Show kernel error messages:

`sudo dmesg --level err`

- Show kernel messages and keep reading new ones, similar to `tail -f` (available in kernels 3.5.0 and newer):

`sudo dmesg -w`

- Show how much physical memory is available on this system:

`sudo dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`sudo dmesg | less`

- Show kernel messages with a timestamp (available in kernels 3.5.0 and newer):

`sudo dmesg -T`

- Show kernel messages in human-readable form (available in kernels 3.5.0 and newer):

`sudo dmesg -H`

- Colorize output (available in kernels 3.5.0 and newer):

`sudo dmesg -L`
