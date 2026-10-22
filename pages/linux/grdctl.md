# grdctl

> Manage GNOME Remote Desktop service.
> More information: <https://github.com/GNOME/gnome-remote-desktop/blob/main/man/grdctl.txt>.

- List the current GRD settings:

`grdctl status`

- Enable Remote Desktop Protocol (RDP) or Virtual Network Computing (VNC) backend services:

`grdctl {{rdp|vnc}} enable`

- Set RDP credentials:

`grdctl rdp set-credentials {{username}} {{password}}`

- Set VNC password:

`grdctl vnc set-password {{password}}`

- Enable remote control of input devices:

`grdctl {{rdp|vnc}} disable-view-only`

- Disable remote control of input devices:

`grdctl {{rdp|vnc}} enable-view-only`

- Disable Remote Desktop Protocol (RDP) or Virtual Network Computing (VNC) backend services:

`grdctl {{rdp|vnc}} disable`
