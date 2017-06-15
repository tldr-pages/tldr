# update-rc.d

> Install and remove System-V style init script links.

- Install a service:

`update-rc.d {{name}} defaults`

- Forcibly remove a service:

`update-rc.d -f {{name}} remove`
 
- Disable a service:

`update-rc.d {{name}} disable`
 
- Enable a service:

`update-rc.d {{name}} enable`
