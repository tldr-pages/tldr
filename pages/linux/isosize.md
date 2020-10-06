# isosize

> Display the size of an ISO file.
> More information: <https://linux.die.net/man/8/isosize>.

- Display the size of an ISO file:

`isosize {{path/to/file.iso}}`

- Diplay the block count and block size of an ISO file:

`isosize --sectors {{path/to/file.iso}}`

- Display the size of an ISO file divided by a given number (only usable when --sectors is not given):

`isosize --divisor={{number}} {{path/to/file.iso}}`
