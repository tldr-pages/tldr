# rdesktop

> Remote Desktop Protocol client.
> It can be used to connect the remote computer using the RDP protocol.

- Connect to a remote computer (default port is 3389):

`rdesktop -u {{username}} -p {{password}} {{host:port}}`

- Simple Examples:

`rdesktop -u Administrator -p passwd123 192.168.1.111:3389`

- Connect to a remote computer with full screen (press `Ctrl + Alt + Enter` to exist):

`rdesktop -u {{username}} -p {{password}} -f {{host:port}}`

- Use the customed resolution (use the letter 'x' between the number):

`rdesktop -u {{username}} -p {{password}} -g 1366x768 {{host:port}}`

- Connect to a remote computer using domain user:

`rdesktop -u {{username}} -p {{password}} -d {{domainname}} {{host:port}}`

- Use the 16 bit color (speed up):

`rdesktop -u {{username}} -p {{password}} -a 16 {{host:port}}`
