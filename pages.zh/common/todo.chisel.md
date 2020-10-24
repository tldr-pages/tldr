# chisel

> Create TCP tunnels. Includes both client and server.
> More information: <https://github.com/jpillora/chisel>.

- Run a Chisel server:

`chisel server`

- Run a Chisel server listening to a specific port:

`chisel server -p {{server_port}}`

- Run a chisel server that accepts authenticated connections using username and password:

`chisel server --auth {{username}}:{{password}}`

- Connect to a Chisel server and tunnel a specific port to a remote server and port:

`chisel client {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- Connect to a Chisel server and tunnel a specific host and port to a remote server and port:

`chisel client {{server_ip}}:{{server_port}} {{local_host}}:{{local_port}}:{{remote_server}}:{{remote_port}}`

- Connect to a Chisel server using username and password authentication:

`chisel client --auth {{username}}:{{password}} {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`
