# hyprcursor-util

> Utility to create and extract Hyprcursor cursor themes for Hyprland.
> More information: <https://github.com/hyprwm/hyprcursor/blob/main/hyprcursor-util/README.md>.

- Compile a working directory into a Hyprcursor theme:

`hyprcursor-util {{[-c|--create]}} {{path/to/theme_directory}}`

- Extract an XCursor theme into a Hyprcursor working directory:

`hyprcursor-util {{[-e|--extract]}} {{path/to/xcursor_theme}}`

- Specify the output directory:

`hyprcursor-util {{[-c|--create]}} {{path/to/theme_directory}} {{[-o|--output]}} {{path/to/output}}`

- Extract a theme with a specific resize mode:

`hyprcursor-util --extract {{path/to/xcursor_theme}} --resize {{none|nearest|bilinear}}`
