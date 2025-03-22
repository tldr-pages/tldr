# ipcs

> Show information about the usage of System V IPC facilities: shared memory segments, message queues, and semaphore arrays.
> See also: `lsipc` for a more flexible tool, `ipcmk` for creating IPC facilities, and `ipcrm` for deleting them.
> More information: <https://manned.org/ipcs>.

- Show information about all active IPC facilities:

`ipcs`

- Show information about active shared [m]emory segments, message [q]ueues or [s]empahore sets:

`ipcs {{--shmems|--queues|--semaphores}}`

- Show full details on the resource with a specific ID:

`ipcs {{--shmems|--queues|--semaphores}} {{[-i|--id]}} {{resource_id}}`

- Show limits in [b]ytes or in a human-readable format:

`ipcs {{[-l|--limits]}} {{--bytes|--human}}`

- Show s[u]mmary about current usage:

`ipcs {{[-u|--summary]}}`

- Show creator's and owner's UIDs and PIDs for all IPC facilities:

`ipcs {{[-c|--creator]}}`

- Show the PID of the last operators for all IPC facilities:

`ipcs {{[-p|--pid]}}`

- Show last access times for all IPC facilities:

`ipcs {{[-t|--time]}}`
