# wtype

> Simulate keyboard input on Wayland, similar to `xdotool type` for X11.
> More information: <https://github.com/atx/wtype>.

- Type text:

`wtype "{{Hello World}}"`

- Type a specific key:

`wtype -k {{Left}}`

- Press a modifier (e.g., "shift", "ctrl"):

`wtype -M {{ctrl}}`

- Release a modifier:

`wtype -m {{ctrl}}`

- Delay between keystrokes (in milliseconds):

`wtype -d {{500}} -- "{{text}}"`

- Read text from stdin:

`echo "{{text}}" | wtype -`
