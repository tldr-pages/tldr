# nc

> Netcat is a versatile utility for working with TCP or UDP data.
> More information: <https://nmap.org/ncat>.

- Listen on a specified port and print any data received:

`nc -l {{port}}`

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

- Scan the open ports of a specified host:

`nc -v -z {{ip_address}} {{port}}`

- Act as proxy and forward data from a local TCP port to the given remote host:

`nc -l {{local_port}} | nc {{hostname}} {{remote_port}}`
