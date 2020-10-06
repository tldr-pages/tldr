# isosize

> Display the size of an iso file. More information: https://linux.die.net/man/8/isosize.

- Display the size of an ISO file:

`isosize {{path/to/file.iso}}`

- Diplay the block count and block size of an iso file:

`isosize --sectors {{path/to/file.iso}}`

- Display the size of an iso file divided by a given number (only usable when -x is not given):

`isosize -d {{number}} {{path/to/file.iso}}`
