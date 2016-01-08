# ping

> Send ICMP ECHO_REQUEST packets to network hosts.

- Ping host:

`ping {{host}}`

- Ping host limiting the number of packages to be send to four:

`ping -c 4 {{host}}`

- Ping host, waiting for 0.5 s between each request (default is 1 s):

`ping -i 0.5 {{host}}`

- Ping host without trying to lookup symbolic names for addresses:

`ping -n {{host}}`
