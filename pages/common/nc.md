# nc

> Netcat is a versatile utility for working with TCP or UDP data.
> More information: <https://manned.org/man/nc.1>.

- Establish a TCP connection:

`nc {{ip_address}} {{port}}`

- Set a timeout:

`nc -w {{timeout_in_seconds}} {{ipaddress}} {{port}}`

- Scan the open TCP ports of a specified host:

`nc -v -z {{ip_address}} {{port}}`

- Listen on a specified TCP port and print any data received:

`nc -l {{port}}`

- Keep the server up after the client detaches:

`nc -k -l {{port}}`

- Listen on a specified UDP port and print connection details and any data received:

`nc -u -l {{port}}`

- Act as proxy and forward data from a local TCP port to the given remote host:

`nc -l {{local_port}} | nc {{hostname}} {{remote_port}}`

- Send a HTTP request:

`echo -e "GET / HTTP/1.1\nHost: {{hostname}}\n\n" | nc {{hostname}} 80`
