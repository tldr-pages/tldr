# netsh interface portproxy

> Configure and display the status of various network components.
> More information: <https://learn.microsoft.com/windows-server/networking/technologies/netsh/netsh-interface-portproxy>.

- Display the current port forwarding setup:

`netsh interface portproxy show all`

- Set up IPv4 port forwarding (run in elevated console):

`netsh interface portproxy add v4tov4 listenaddress={{192.168.0.1}} listenport={{8080}}  connectaddress={{10.0.0.1}} connectport={{80}}`

- Remove IPv4 port forwarding (run in elevated console):

`netsh interface portproxy delete v4tov4 listenaddress={{192.168.0.1}} listenport={{8080}}`

- Display help:

`netsh interface portproxy`
