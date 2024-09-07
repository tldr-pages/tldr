# ipcs

> Show information about the usage of System V IPC facilities: shared memory segments, message queues, and semaphore arrays.
> See also: `lsipc` for a more flexible tool, `ipcmk` for creating IPC facilities, and `ipcrm` for deleting them.
> More information: <https://manned.org/ipcs>.

- Show information about all active IPC facilities:

`ipcs`

- Show information about active shared [m]emory segments, message [q]ueues or [s]empahore sets:

`ipcs {{--shmems|--queues|--semaphores}}`

- Show full details on the resource with a specific [i]D:

`ipcs {{--shmems|--queues|--semaphores}} --id {{resource_id}}`

- Show [l]imits in [b]ytes or in a human-readable format:

`ipcs --limits {{--bytes|--human}}`

- Show s[u]mmary about current usage:

`ipcs --summary`

- Show [c]reator's and owner's UIDs and PIDs for all IPC facilities:

`ipcs --creator`

- Show the [p]ID of the last operators for all IPC facilities:

`ipcs --pid`

- Show last access [t]imes for all IPC facilities:

`ipcs --time`
