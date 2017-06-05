# fping

> A more powerful ping which can ping multiple hosts.

- List alive hosts within a given subnet using a netmask:

`fping -a -g 192.168.1.0/24`

- List alive hosts within a given subnet using a IP range:

`fping -a -g 192.168.1.1 192.168.1.254`

- List unreachable hosts within a given subnet:

`fping -u -g 192.168.1.0/24`
