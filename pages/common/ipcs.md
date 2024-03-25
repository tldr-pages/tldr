# ipcs

> Show information about the usage of XSI IPC facilities: shared memory segments, message queues, and semaphore arrays.
> More information: <https://manned.org/ipcs.1p>.

- Show information about all the IPC:

`ipcs -a`

- Show information about active shared [m]emory segments, message [q]ueues or [s]empahore sets:

`ipcs {{-m|-q|-s}}`

- Show information on maximum allowable size in [b]ytes:

`ipcs -b`

- Show [c]reator’s user name and group name for all IPC facilities:

`ipcs -c`

- Show the [p]ID of the last operators for all IPC facilities:

`ipcs -p`

- Show access [t]imes for all IPC facilities:

`ipcs -t`

- Show [o]utstanding usage for active message queues, and shared memory segments:

`ipcs -o`
