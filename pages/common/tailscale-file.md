# tailscale file

> Send files across connected devices on a Tailscale network.
> It currently does not support sending files to devices owned by other users even on the same Tailscale network.
> More information: <https://tailscale.com/kb/1106/taildrop/>.

- Send a file to a specific node:

`sudo tailscale file cp {{path/to/file}} {{hostname|ip}}:`

- Store files that were sent to the current node into a specific directory:

`sudo tailscale file get {{path/to/directory}}`
