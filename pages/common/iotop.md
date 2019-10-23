# iotop

> Display a table of current I/O usage by processes or threads.
> More information: <https://linux.die.net/man/1/iotop>.

- Start top-like I/O monitor:

`iotop`

- Show only processes or threads actually doing I/O:

`iotop -o`

- Show I/O usage in non-interactive mode:

`iotop -b`

- Show only I/O usage of processes(Default is to show all threads):

`iotop -P`

- Show I/O usage of given PID(s):

`iotop -p {{PID}}`

- Show I/O usage of a given user:

`iotop -u {{user}}`

- Show accumulated I/O instead of bandwidth:

`iotop -a`
