# bottom

> A cross-platform graphical process/system monitor.
> An alternative to top, htop, and other system monitors.
> More information: <https://github.com/ClementTsang/bottom>.

- Start bottom:

`btm`

- Start bottom with default widget layout:

`btm --default_widget_type {{cpu}}`

- Show processes as a tree:

`btm --tree`

- Show only processes matching a regex:

`btm --regex {{pattern}}`

- Start in basic mode (disable graphs, use less CPU):

`btm --basic`

- Show battery information (if available):

`btm --battery`

- Set the update rate in milliseconds:

`btm --rate {{1000}}`

- Use a specific color scheme:

`btm --color {{default|default-light|gruvbox|gruvbox-light|nord|nord-light}}`
