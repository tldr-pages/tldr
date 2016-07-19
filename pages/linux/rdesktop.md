# RDESKTOP

> Remote Desktop Protocal client.
> It can be used to connect remote windows server or PC using RDP protocal.

- Connect to a remote computer, default port is 3389:

`rdesktop -u {{username}} -p {{password}} {{host:port}}`

- simple Examples:

`rdesktop -u Administrator -p passwd123 192.168.1.111:3389`

- Connect to a remote computer with full screen, you need the press `Ctrl+Alt+Enter` to exist the window:

`rdesktop -u {{username}} -p {{password}} -f {{host:port}}`

- use the customed resolution, (use the letter 'x' between the number):

`rdesktop -u {{username}} -p {{password}} -g 1366x768 {{host:port}}`

- connect to a remote computer using domain user:

`rdesktop -u {{username}} -p {{password}} -d {{domainname}} {{host:port}}`

- use the 16 bit color (speed up):

`rdesktop -u {{username}} -p {{password}} -a 16 {{host:port}}`
