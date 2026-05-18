# walker

> A Wayland-native application launcher and runner with pluggable providers.
> See also: `fuzzel`, `wofi`, `rofi`.
> More information: <https://github.com/abenz1267/walker>.

- Open the launcher:

`walker`

- Restrict the launcher to a single provider (e.g. `desktopapplications`, `calc`, `clipboard`, `runner`):

`walker {{[-m|--provider]}} {{desktopapplications}}`

- Read items from `stdin` and print the selected item to `stdout` (dmenu mode):

`printf "{{Choice1\nChoice2\nChoice3}}" | walker {{[-d|--dmenu]}}`

- Open the launcher with a specific theme:

`walker {{[-t|--theme]}} {{theme_name}}`
