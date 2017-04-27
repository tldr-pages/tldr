# telnet

> Connect to a specified port of a host using the telnet protocol.

- Telnet to a certain port:

`telnet  {{ip_address}} {{port}}`

- Exit a telnet session:

`quit`

- Emit the default escape character:

`CTRL + ]`

- Start telnet with "x" as the escape character:

`telnet -e {{x}} {{ip_address}} {{port}}`
