# xhost

> Manage access control lists for X server connections.
> More information: <https://manned.org/xhost>.

- Display the current access control list:

`xhost`

- Allow a specific host to connect to the X server:

`xhost +{{hostname}}`

- Deny a specific host from connecting to the X server:

`xhost -{{hostname}}`

- Allow all hosts to connect (disable access control - insecure):

`xhost +`

- Deny all hosts except those explicitly allowed (enable access control):

`xhost -`

- Remove a specific user or address using a family prefix (like `inet:hostname` or `si:localuser:username`):

`xhost -{{family:name}}`
