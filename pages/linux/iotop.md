# iotop

> Display a table of current I/O usage by processes or threads.
> More information: <https://linux.die.net/man/1/iotop>.

- Start top-like I/O monitor:

`iotop`

- Only show processes or threads actually doing I/O:

`iotop -o`

- Show I/O usage in non-interactive mode:

`iotop -b`

- Only I/O usage of processes(Normally iotop shows all threads):

`iotop -P`

- Show I/O usage of given PID(s):

`iotop -p {{PID}}`

- Show I/O usage of given USER:

`iotop -u {{USER}}`

- Show accumulated I/O instead of bandwidth:

`iotop -a`
