# ssh

> Create a secure link to a remote machine for remote administration
> More information: <https://manned.org/ssh>.

- Simple SSH into a remote machine/server:

`ssh :{{user}}@:{{remoteServer}} -p:{{port}}`

- Local Port Forwarding:

`ssh -L :{{remotePort}}::{{localhost}}::{{localPort}} :{{user}}@{{remoteServer}} -p:{{port}}`

- Remote Port Forwarding

`ssh -R :{{remotePort}}::{{localhost}}::{{localPort}} :{{user}}@:{{remoteServer}} -p:{{port}}`

- Use custom Key Algorithms

`ssh -o:{{Algorithm}} :{{user}}@:{{remoteServer}} -p:{{port}}`
