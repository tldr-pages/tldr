# upnpc

> Configure port forwarding rules on your router via the UPnP protocol.
> More information: <https://manned.org/upnpc>.

- Forward the external TCP port 80 to port 8080 on a local machine:

`upnpc -a {{192.168.0.1}} 8080 80 tcp`

- Delete any port redirection for external TCP port 80:

`upnpc -d 80 tcp`

- Get information about UPnP devices on your network:

`upnpc -s`

- List existing redirections:

`upnpc -l`
