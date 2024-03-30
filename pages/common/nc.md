# nc

> A versatile utility for redirecting IO into a network stream.
> More information: <https://manned.org/man/nc.1>.

- Start a listener on the specified TCP port and send a file into it:

`nc -l -p {{port}} < {{filename}}`

- Connect to a target listener on the specified port and receive a file from it:

`nc {{host}} {{port}} > {{received_filename}}`

- Scan the open TCP ports of a specified host:

`nc -v -z -w {{timeout_in_seconds}} {{host}} {{start_port}}-{{end_port}}`

- Start a listener on the specified TCP port and provide your local shell access to the connected party (this is dangerous and can be abused):

`nc -l -p {{port}} -e {{shell_executable}}`

- Connect to a target listener and provide your local shell access to the remote party (this is dangerous and can be abused):

`nc {{host}} {{port}} -e {{shell_executable}}`

- Act as a proxy and forward data from a local TCP port to the given remote host:

`nc -l -p {{local_port}} | nc {{host}} {{remote_port}}`

- Send an HTTP GET request:

`echo -e "GET / HTTP/1.1\nHost: {{host}}\n\n" | nc {{host}} 80`
