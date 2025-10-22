# wev

> Print contents of Wayland events.
> More information: <https://manned.org/wev>.

- Monitor all occurring Wayland events:

`wev`

- Print all events received by a specific Wayland interface:

`wev -f {{wl_keyboard}}`

- Print only specific events received by a Wayland interface:

`wev -f {{wl_keyboard}}:{{key}}`

- Print everything but the specified wayland events:

`wev -F {{wl_keyboard}}:{{key}}`

- Write the `wl_keyboards`'s keymap to a file:

`wev -M {{path/to/file}}`

- Print Wayland globals:

`wev -g`
