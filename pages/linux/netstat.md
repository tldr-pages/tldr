# netstat

> Displays network-related information such as open connections, open socket ports, etc.
> More information: <https://man7.org/linux/man-pages/man8/netstat.8.html>.

- List all ports:

`netstat --all`

- List all listening ports:

`netstat --listening`

- List listening TCP ports:

`netstat --tcp`

- Display PID and program names:

`netstat --program`

- List information continuously:

`netstat --continuous`

- List routes and do not resolve IP addresses to hostnames:

`netstat --route --numeric`

- List listening TCP and UDP ports (+ user and process if you're root):

`netstat --listening --program --numeric --tcp --udp --extend`
