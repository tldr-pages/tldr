# x11vnc

> A VNC server for real X Displays.

- Launch a VNC server that allows multiple clients to connect:

`x11vnc -shared`

- Launch a VNC server that will continue after a disconnect in view only mode:

`x11vnc -forever -viewonly`

- Launch a VNC server on a specific display and screen:

`x11vnc -display :{{screen}}.{{display}}`
