# netstat

> Display network-related information such as open connections, open socket ports, etc.
> See also: `ss`.
> More information: <https://manned.org/netstat>.

- List all ports:

`netstat {{[-a|--all]}}`

- List all listening ports:

`netstat {{-l|--listening]}}`

- List listening TCP ports:

`netstat {{-t|--tcp]}}`

- Display PID and program names:

`netstat {{[-p|--program]}}`

- List information continuously:

`netstat {{[-c|--continuous]}}`

- List routes and do not resolve IP addresses to hostnames:

`netstat {{[-rn|--route --numeric]}}`

- List listening TCP and UDP ports (+ user and process if you're root):

`netstat {{[-tulpne|--tcp --udp --listening --program --numeric --extend]}}`
