# upnpc

> Configure port forwarding rules on your router via the UPnP protocol.
> More information: <http://miniupnp.free.fr/>.

- Forward external TCP port 80 to port 8080 on a local machine:

`upnpc -a {{xxx.xxx.xxx.xxx}} 8080 80 tcp`

- Delete any port redirection for external TCP port 80:

`upnpc -d 80 tcp`

- Get information about UPnP devices on your network:

`upnpc -s`

- List existing redirections:

`upnpc -l`
