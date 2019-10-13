# chisel

> Chisel is a tool creating a TCP tunnel. Including both client and server.
> More information: <https://github.com/jpillora/chisel>.

- Run a chisel server:

`chisel server`

- Run a chisel server listening to a specific port:

`chisel server -p {{server_port}}`

- Run a chisel server securing the connection using a username and password authentication:

`chisel server --auth {{username}}:{{password}}`

- Connect to a chisel server and tunnel a specific port to a remote server and port:

`chisel client {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`

- Connect to a chisel server and tunnel a specific host and port to a remote server and port:

`chisel client {{server_ip}}:{{server_port}} {{local_host}}:{{local_port}}:{{remote_server}}:{{remote_port}}`

- Connect to a chisel server using username and password authentication:

`chisel client --auth {{username}}:{{password}} {{server_ip}}:{{server_port}} {{local_port}}:{{remote_server}}:{{remote_port}}`
