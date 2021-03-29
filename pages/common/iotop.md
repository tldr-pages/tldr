# iotop

> Display a table of current I/O usage by processes or threads.
> More information: <https://man.archlinux.org/man/iotop.8>.

- Start top-like I/O monitor:

`sudo iotop`

- Show only processes or threads actually doing I/O:

`sudo iotop --only`

- Show I/O usage in non-interactive mode:

`sudo iotop --batch`

- Show only I/O usage of processes (default is to show all threads):

`sudo iotop --processes`

- Show I/O usage of given PID(s):

`sudo iotop --pid={{PID}}`

- Show I/O usage of a given user:

`sudo iotop --user={{user}}`

- Show accumulated I/O instead of bandwidth:

`sudo iotop --accumulated`
