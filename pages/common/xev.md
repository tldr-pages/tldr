# xev

> Print contents of X events.
> More information: <https://gitlab.freedesktop.org/xorg/app/xev>.

- Monitor all occuring X events:

`xev`

- Monitor all X events of the root window instead of creating a new one:

`xev -root`

- Monitor all X events of a particular window:

`xev -id {{window_id}}`

- Monitor X events from a given category (can be specified multiple times):

`xev -event {{event_category}}`
