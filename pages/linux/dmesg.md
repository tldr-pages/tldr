# dmesg

> Write the kernel messages to standard output.

- Show kernel messages:

`dmesg`

- Show kernel messages and follow output(work as `tail -f` | (since kernel 3.5.0)):

`dmesg -w`

- Show how much physical memory is available on this system:

`dmesg | grep -i memory`

- Show kernel messages 1 page at a time:

`dmesg | less`
