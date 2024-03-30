# nettop

> Display updated information about the network.
> More information: <https://keith.github.io/xcode-man-pages/nettop.1.html>.

- Monitor TCP and UDP sockets from all interfaces:

`nettop`

- Monitor TCP sockets from Loopback interfaces:

`nettop -m {{tcp}} -t {{loopback}}`

- Monitor a specific process:

`nettop -p "{{process_id|process_name}}"`

- Display a per-process summary:

`nettop -P`

- Print 10 samples of network information:

`nettop -l {{10}}`

- Monitor changes every 5 seconds:

`nettop -d -s {{5}}`

- While running nettop, list interactive commands:

`h`

- Display help:

`nettop -h`
