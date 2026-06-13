# xprop

> Display window and font properties in an X server.
> More information: <https://manned.org/xprop>.

- Display the name of the root window:

`xprop -root WM_NAME`

- Display the window manager hints for a window:

`xprop -name "{{window_name}}" WM_HINTS`

- Display the point size of a font:

`xprop -font "{{font_name}}" POINT_SIZE`

- Display all the properties of the window with the ID 0x200007:

`xprop -id {{0x200007}}`
