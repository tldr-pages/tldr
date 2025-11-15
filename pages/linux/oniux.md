# oniux

> Isolate an arbitrary application and route traffic over the Tor network.
> Note: This is experimental software.
> More information: <https://gitlab.torproject.org/tpo/core/oniux>.

- Isolate an application:

`oniux {{command}}`

- Query a website:

`oniux curl {{https://example.com}}`

- Query an onion site:

`oniux curl {{http://example.onion}}`

- Run an entire shell in "torified" isolation:

`oniux bash`

- Isolate graphical applications in desktop environments:

`oniux hexchat`
