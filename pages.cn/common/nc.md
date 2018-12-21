# nc

> Reads and writes tcp or udp data.

- Listen on a specified port:

`nc  -l {{port}}`

- Connect to a certain port (you can then write to this port):

`nc {{ip_address}} {{port}}`

- Set a timeout:

`nc -w {{timeout_in_seconds}} {{ipaddress}} {{port}}`

- Serve a file:

`nc -l {{port}} < {{file}}`

- Receive a file:

`nc {{ip_address}} {{port}} > {{file}}`

- Server stay up after client detach:

`nc -k -l {{port}}`

- Client stay up after EOF:

`nc -q {{timeout}} {{ip_address}}`

- Port scanning:

`nc -v -z {{ip_address}} {{port}}`

- Proxy and port forwarding:

`nc -l {{port}} | nc {{hostname}} {{port}}`
