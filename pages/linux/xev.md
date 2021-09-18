# xev

> Print contents of X events.
> More information: <https://gitlab.freedesktop.org/xorg/app/xev>.

- View all occuring X events:

`xev`

- Monitor the X events of the root window instead of creating a new one:

`xev --root`

- View the X events of a particular window:

`xev -id {{Window_id}}`

- View a category of X events (multiple flags can be chained):

`xev --event {{Event_category}}`
