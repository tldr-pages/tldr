# netstat

> Display network-related information such as open connections, open socket ports, etc.
> See also: `ss`.
> More information: <https://manned.org/netstat>.

- List all ports:

`netstat {{[-a|--all]}}`

- List all listening ports:

`netstat {{-l|--listening]}}`

- List listening TCP ports:

`netstat --tcp`

- Display PID and program names:

`netstat --program`

- List information continuously:

`netstat --continuous`

- List routes and do not resolve IP addresses to hostnames:

`netstat --route --numeric`

- List listening TCP and UDP ports (+ user and process if you're root):

`netstat {{[-lpntue|--listening --program --numeric --tcp --udp --extend]}}`
