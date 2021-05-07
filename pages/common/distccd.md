# distccd

> Server daemon for distcc distributed compiler.
> More information: <https://distcc.github.io>.

- Start a daemon with default settings:

`distccd --daemon`

- Start a daemon, accepting connections from private network IPv4 ranges:

`distccd --daemon --allow-private`

- Start a daemon accepting connections from specific network address or address range:

`distccd --daemon --allow {{IP[/BITS]}}`

- Start a daemon with a maximum of 4 tasks at any time and lowered priority (niceness = 5):

`distccd --daemon --jobs {{4}} --nice {{5}}`

- Start a daemon and register via mDNS/DNS-SD (Zeroconf):

`distccd --daemon --zeroconf`
