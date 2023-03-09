# netcat

> Network (diagnostic) tool.
> Can be used to receive and send data via TCP and UDP.
> More information: <https://salsa.debian.org/debian/netcat-openbsd>.

- Establish a TCP connection to 127.0.0.1:1234:

`netcat {{127.0.0.1}} {{1234}}`

- Connect via UDP to to [::1]:1235:

`netcat -u {{::1}} {{1235}}`

- Send a HTTP request to example.com:

`echo -e "GET / HTTP/1.1\nHost: {{example.com}}\n\n" | netcat {{example.com}} 80`

- Connect to 192.0.2.7 over IPv4-only:

`netcat -4 {{192.0.2.7}}`

- Enable verbose output:

`netcat -v {{192.0.2.67}}`

- Listen on TCP Port 1236:

`netcat -l {{1236}}`

- Listen on UDP port 1239 and listen on another one after the current one is finished:

`netcat -lku {{1239}}`

- On systems without or with faulty DNS, errors may occur. Disabling DNS resolution can solve the problem:

`netcat -n {{127.0.1.1}} {{1234}}`
