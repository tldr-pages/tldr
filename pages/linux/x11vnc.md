# x11vnc

> A VNC server that will enable VNC on an existing display.


- Launch a VNC server that allows multiple clients to connect:

`x11vnc -shared`

- Launch a VNC server that will not exist after a client disconnects:

`x11vnc -forever -viewonly`

- Launch the server where the user can only view the screen, and will continue to run even after the last client disconnects:

`x11vnc -display :{{screen}}.{{display}}`

- Launch a VNC server on screen 2 with the default display:

`x11vnc -display :2`

- Launch a VNC server on the second monitor:

`x11vnc -display :0.1`
