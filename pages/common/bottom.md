# bottom

> A graphical process and system monitor with a customizable interface.
> More information: <https://clementtsang.github.io/bottom>.

- Start bottom with default settings:

`btm`

- Start bottom in basic mode (similar to htop):

`btm --basic`

- Start bottom with a specific refresh rate in milliseconds:

`btm --rate {{1000}}`

- Start bottom with CPU usage shown as a percentage per core:

`btm --cpu_left_legend`

- Start bottom with the process widget in tree mode:

`btm --tree`

- Start bottom and show only CPU, memory, and process widgets:

`btm --default_widget_type {{cpu}} --default_widget_count {{3}}`

- Start bottom with a custom configuration file:

`btm --config {{path/to/config.toml}}`

- Display help:

`btm --help`
