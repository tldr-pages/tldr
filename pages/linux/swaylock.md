# swaylock

> Screen locking utility for Wayland compositors.
> More information: <https://manned.org/swaylock>.

- Lock the screen showing a white background:

`swaylock`

- Lock the screen with a simple color background (rrggbb format):

`swaylock --color {{0000ff}}`

- Lock the screen to a PNG background:

`swaylock --image {{path/to/file.png}}`

- Lock the screen and disable the unlock indicator (removes feedback on keypress):

`swaylock --no-unlock-indicator`

- Lock the screen and don't hide the mouse pointer:

`swaylock --pointer {{default}}`

- Lock the screen to a PNG background tiled over all monitors:

`swaylock --image {{path/to/file.png}} --tiling`

- Lock the screen and show the number of failed login attempts:

`swaylock --show-failed-attempts`

- Load configuration from a file:

`swaylock --config {{path/to/config}}`
