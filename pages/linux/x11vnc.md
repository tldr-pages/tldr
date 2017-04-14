# x11vnc

> A VNC server that will enable VNC on an existing display.
> By default, the server will automatically terminate once all clients disconnect from it.

- Launch a VNC server that allows multiple clients to connect:

`x11vnc -shared`

- Launch a VNC server in view-only mode, and which won't terminate once the last client disconnects:

`x11vnc -forever -viewonly`

- Launch a VNC server on a specific display and screen:

`x11vnc -display :{{screen}}.{{display}}`

- Launch a VNC server on screen 2 with the default display:

`x11vnc -display :{{2}}`

- Launch a VNC server on the second monitor:

`x11vnc -display :{{0}}.{{1}}`
