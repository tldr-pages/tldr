# distccd

> Server daemon for the distcc distributed compiler.
> More information: <https://distcc.github.io>.

- Start a daemon with the default settings:

`distccd --daemon`

- Start a daemon, accepting connections from IPv4 private network ranges:

`distccd --daemon --allow-private`

- Start a daemon, accepting connections from a specific network address or address range:

`distccd --daemon --allow {{ip_address|network_prefix}}`

- Start a daemon with a lowered priority that can run a maximum of 4 tasks at a time:

`distccd --daemon --jobs {{4}} --nice {{5}}`

- Start a daemon and register it via mDNS/DNS-SD (Zeroconf):

`distccd --daemon --zeroconf`
