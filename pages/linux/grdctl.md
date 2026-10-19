# grdctl

> Manage GNOME Remote Desktop service.
> More information: <https://github.com/GNOME/gnome-remote-desktop>.

- List the current GRD settings:

`rdctl status`

- Enable Remote Desktop Protocol (RDP) backend service:

`grdctl rdp enable`

- Set RDP credentials:

`grdctl set-credentials [<username>] [<password>]`

- Enable Virtual Network Computing (VNC) backend service:

`grdctl vnc enable`

- Set VNC password:

`grdctl set-password [<password>]`

- Enable remote control of input devices:

`grdctl [<rdp>/<vnc>] disable-view-only`
