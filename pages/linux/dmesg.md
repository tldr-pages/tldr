# dmesg

> Write the kernel messages to standard output.

- Show kernel messages:

`dmesg`

- Show kernel messages and keep reading new ones, similar to `tail -f` (available in kernels 3.5.0 and newer):

`dmesg -w`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`
