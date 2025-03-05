# iotop

> Display a table of current I/O usage by processes or threads.
> More information: <https://manned.org/iotop>.

- Start top-like I/O monitor:

`sudo iotop`

- Show only processes or threads actually doing I/O:

`sudo iotop {{[-o|--only]}}`

- Show I/O usage in non-interactive mode:

`sudo iotop {{[-b|--batch]}}`

- Show only I/O usage of processes (default is to show all threads):

`sudo iotop {{[-P|--processes]}}`

- Show I/O usage of given PID(s):

`sudo iotop {{[-p|--pid]}} {{PID}}`

- Show I/O usage of a given user:

`sudo iotop {{[-u|--user]}} {{user}}`

- Show accumulated I/O instead of bandwidth:

`sudo iotop {{[-a|--accumulated]}}`
