# Palworld

> Create and start a headless Palworld server.
> More information: <https://docs.palworldgame.com/settings-and-operation/arguments>.

- Start the server with default settings:

`{{path/to/PalServer.sh}}`

- Start the server with a specific port and a specific number of players:

`{{path/to/PalServer.sh}} -port={{8211}} -players={{1..32}}`

- Start a public lobby server:

`{{path/to/PalServer.sh}} -publiclobby`

- Start the server with performance optimizations for multi-threaded CPUs:

`{{path/to/PalServer.sh}} -useperfthreads -NoAsyncLoadingThread -UseMultithreadForDS`

- Start the server with a specific public IP and port for community servers:

`{{path/to/PalServer.sh}} -publicip={{ip_address}} -publicport={{port}}`
