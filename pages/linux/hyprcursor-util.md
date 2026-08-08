# hyprcursor-util

> Utility to create and extract Hyprcursor cursor themes for Hyprland.
> More information: <https://wiki.hypr.land/Hypr-Ecosystem/hyprcursor/>.

- Compile a working directory into a Hyprcursor theme:

`hyprcursor-util --create {{path/to/theme_directory}}`

- Extract an XCursor theme into a Hyprcursor working directory:

`hyprcursor-util --extract {{path/to/xcursor_theme}}`

- Specify the output directory:

`hyprcursor-util --create {{path/to/theme_directory}} --output {{path/to/output}}`

- Extract a theme with a specific resize mode (`none`, `bilinear`, or `nearest`):

`hyprcursor-util --extract {{path/to/xcursor_theme}} --resize {{bilinear}}`
