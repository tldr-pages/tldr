# update-rc.d

> Install and remove System-V style init script links

- Installing a service:

`update-rc.d {{name}} defaults`

- Removing a service forcibly:

`update-rc.d -f {{name}} remove`
 
- Disabling a service:

`update-rc.d {{name}} disable`
 
- Enabling a service:

`update-rc.d {{name}} enable`
