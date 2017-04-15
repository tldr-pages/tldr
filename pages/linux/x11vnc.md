# x11vnc

> A VNC server that will enable VNC on an existing display ser.
> By default, the server will automatically terminate once all clients disconnect from it.

- Launch a VNC server that allows multiple clients to connect:

`x11vnc -shared`

- Launch a VNC server in view-only mode, and which won't terminate once the last client disconnects:

`x11vnc -forever -viewonly`

- Launch a VNC server on a specific display and screen (both starting at index zero):

`x11vnc -display :{{display}}.{{screen}}`

- Launch a VNC server on the third display's default screen:

`x11vnc -display :{{2}}`

- Launch a VNC server on the first display's second screen:

`x11vnc -display :{{0}}.{{1}}`
