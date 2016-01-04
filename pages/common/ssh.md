# SSH

> Secure Shell is a protocol used to securely log onto remote systems.
> It can be used for logging or executing commands on a remote server.

- connecting to a remote server

`ssh {{username}}@{{remote_host}}`

- connecting to a remote server with a specific identity (private key)

`ssh -i {{/path/to/key_file}} {{username}}@{{remote_host}}`

- connecting to a remote server with specific port

`ssh {{username}}@{{remote_host}} -p {{2222}}`

- run a command on a remote server

`ssh {{remote_host}} "{{command -with -flags}}"`

- ssh tunneling: dynamic port forwarding (SOCKS proxy on localhost:9999)

`ssh -D {{9999}} -C {{username}}@{{remote_host}}`

- ssh tunneling: forward a specific port (localhost:9999 to slashdot.org:80)

`ssh -L {{9999}}:slashdot.org:80 {{username}}@{{remote_host}}`

- ssh enable agent forward

`ssh -A {{username}}@{{remote_host}}`

- use a jump box as a proxy to log in to a server (not accessible from a public subnet)

`ssh -t {{proxy_host}} ssh {{username}}@{{remote_host}}`

- copy your ssh public key to a server for password-less login without ssh-copy-id

`cat ~/.ssh/id_rsa.pub | ssh {{username}}@{{remote_host}} "mkdir ~/.ssh; cat >> ~/.ssh/authorized_keys"`

- execute list of cmds in a cmd.txt file over ssh

```ssh {{username}}@{{remote_host}} {{user}} "`cat cmd.txt`"```
