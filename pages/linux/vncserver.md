# vncserver

> Launch a VNC (Virtual Network Computing) desktop.
> More information: <https://manned.org/vncserver.1x>.

- Launch a VNC Server on next available display:

`vncserver`

- Launch a VNC Server with specific screen geometry:

`vncserver --geometry {{width}}x{{height}}`

- Kill an instance of VNC Server running on a specific display:

`vncserver --kill :{{display_number}}`
