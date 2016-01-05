# SSH

> Secure Shell is a protocol used to securely log onto remote systems.
> It can be used for logging or executing commands on a remote server.

- connect to an SSH server

`ssh {{username}}@{{remote_host}}`

- connect on a specific port and with specific key file

`ssh -p {{2222}} -i {{/path/to/key_file}} {{remote_host}}`

- run a command on a remote server

`ssh {{remote_host}} {{command -with -flags}}`

- ssh tunneling: dynamic port forwarding (SOCKS proxy on localhost:9999)

`ssh -D {{9999}} {{remote_host}}`

- ssh tunneling: access Slashdot as if on remote_host by connecting to localhost:9999 (To access Slashdot as if on localhost by connecting to remote_host:9999, use -R instead of -L)

`ssh -L {{9999}}:slashdot.org:80 {{remote_host}}`
