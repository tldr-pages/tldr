# krfb-virtualmonitor

> Create a virtual monitor and allow that monitor to be used with VNC.
> More information: <https://invent.kde.org/network/krfb>.

- Create a virtual monitor with dimensions `1920x1080`:

`krfb-virtualmonitor`

- Set the virtual monitor dimensions:
  
`krfb-virtualmonitor --resolution {{1920}}x{{1080}}`

- Set the monitor name:

`krfb-virtualmonitor --name {{monitor_name}}`

- Set the monitor password for remote connection on port `9999`:
 
`krfb-virtualmonitor --password {{password}}`

- Set the password and the port:

`krfb-virtualmonitor --password {{password}} --port {{5900}}`

- Display help:

`krfb-virtualmonitor {{[-h|--help]}}`
