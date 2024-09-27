# fping

> A more powerful ping which can ping multiple hosts.
> More information: <https://fping.org>.

- List alive hosts within a subnet generated from a netmask:

`fping {{-a|--alive}} {{-g|--generate}} 192.168.1.0/24`

- List alive hosts within a subnet generated from an IP range:

`fping {{-a|--alive}} {{-g|--generate}} 192.168.1.1 192.168.1.254`

- List unreachable hosts within a subnet generated from a netmask:

`fping {{-u|--unreach}} {{-g|--generate}} 192.168.1.0/24`
