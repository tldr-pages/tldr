# ping

> Send ICMP ECHO_REQUEST packets to network hosts.
> Unlike Unix-like systems, Windows `ping` sends only 4 packets by default.
> More information: <https://learn.microsoft.com/windows-server/administration/windows-commands/ping>.

- Ping a host 4 times:

`ping {{host}}`

- Ping a host a specific number of times:

`ping -n {{count}} {{host}}`

- Ping a host continuously (until stopped with `<Ctrl c>`):

`ping -t {{host}}`

- Set the timeout in milliseconds to wait for each reply:

`ping -w {{milliseconds}} {{host}}`

- Set the buffer size of the ping packet in bytes:

`ping -l {{bytes}} {{host}}`

- Ping a host using a specific source IP address:

`ping -S {{source_ip}} {{host}}`

- Resolve address to hostname:

`ping -a {{host}}`
