# fping

> A more powerful ping which can ping multiple hosts.
> More information: <https://fping.org/fping.8.html>.

- List the status of all hosts within a range:

`fping {{192.168.1.{1..254}}}`

- List alive hosts within a subnet generated from a netmask:

`fping {{[-a|--alive]}} {{[-g|--generate]}} {{192.168.1.0/24}}`

- List alive hosts within a subnet generated from an IP range and prune per-probe results:

`fping {{[-q|--quiet]}} {{[-a|--alive]}} {{[-g|--generate]}} {{192.168.1.1}} {{192.168.1.254}}`

- List unreachable hosts within a subnet generated from a netmask:

`fping {{[-u|--unreach]}} {{[-g|--generate]}} {{192.168.1.0/24}}`
