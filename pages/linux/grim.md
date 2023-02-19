# grim

> Grab images (Screenshots) from a Wayland compositor
> More information: https://github.com/emersion/grim

- Screenshoot all outputs:

`grim`

- Screenshoot a specific output:

`grim -o {{display_output}}`

- Screenshoot a region:

`grim -g "{{<x>,<y> <width>x<height>}}"`

Select a region and screenshoot it: (using slurp)

`grim -g "{{$(slurp)}}"`

- Use a custom filename:

`grim "{{filepath.png}}"

- Screenshoot and copy to clipboard:

`grim - | {{clipboard_manager}}`

