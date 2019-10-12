# swaymsg

> Send messages to a running instance of sway over the IPC socket.

- Get outputs available to sway:

`swaymsg -t get_outputs`

- Get list of seats:

`swaymsg -t get_seats`

- Send sway command - see sway(5) for list of commands:

`swaymsg -- {{command}}`

- Pretty print JSON data:

`swaymsg --pretty -- {{command}}`

- Specify sway socket path:

`swaymsg --socket {{path/to/socket}} -- {{command}}`
