# oniux

> Isolate an arbitrary application over the Tor network.
> This is still considered experimental software! More information: <https://gitlab.torproject.org/tpo/core/oniux>.

- Perform a simple HTTPS query using oniux:

`oniux curl https://icanhazip.com`

- Perform a simple HTTPS query using oniux, using IPv6:

`oniux curl -6 https://ipv6.icanhazip.com`

- Perform a simple HTTPS query using oniux, on the Tor network:

`oniux curl http://2gzyxa5ihm7nsggfxnu52rck2vv4rvmdlkiu3zzui5du4xyclen53wid.onion/index.html`

- Run an entire shell in a "torified" isolation:

`oniux bash`

- Isolcate graphical applications in desktop environments:

`oniux hexchat`
