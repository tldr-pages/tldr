# uuidd

> Daemon for generating UUIDs.
> More information: <https://manned.org/uuidd>.

- Generate a random UUID:

`uuidd --random`

- Generate a bulk number of random UUIDs:

`uuidd --random --uuids {{number_of_uuids}}`

- Generate a time-based UUID, based on the current time and MAC address of the system:

`uuidd --time`
