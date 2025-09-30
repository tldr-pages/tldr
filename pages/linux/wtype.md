# wtype

> Simulate keyboard input on Wayland, similar to `xdotool type` for X11.
> See also: `ydotool`.
> More information: <https://manned.org/wtype>.

- Simulate typing text:

`wtype "{{Hello World}}"`

- Type a specific key:

`wtype -k {{Left}}`

- Press a modifier:

`wtype -M {{shift|ctrl|...}}`

- Release a modifier:

`wtype -m {{ctrl}}`

- Wait between keystrokes (in milliseconds):

`wtype -d {{500}} -- "{{text}}"`

- Read text from `stdin`:

`echo "{{text}}" | wtype -`
