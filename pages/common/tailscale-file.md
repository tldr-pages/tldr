# tailscale file

> Send files across connected devices on a Tailscale network.
> It currently does not support sending files to devices owned by other users even on the same Tailscale network.
> More information: <https://tailscale.com/kb/1106/taildrop/>.

- Send a file to another device on the Tailscale network:

`sudo tailscale file cp {{path/to/file}} {{hostname_or_ip}}:`

- Receive a file that was sent to the device:

`sudo tailscale file get {{path/to/directory}}`
