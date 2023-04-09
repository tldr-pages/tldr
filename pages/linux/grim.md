# grim

> Grab images (Screenshots) from a Wayland compositor.
> More information: <https://sr.ht/~emersion/grim>.

- Screenshot all outputs:

`grim`

- Screenshot a specific output:

`grim -o {{path/to/output_file}}`

- Screenshot a specific region:

`grim -g "{{<x_position>,<y_position> <width>x<height>}}"`

- Select a specific region and screenshot it, (using slurp):

`grim -g "{{$(slurp)}}"`

- Use a custom filename:

`grim "{{path/to/file.png}}"`

- Screenshot and copy to clipboard:

`grim - | {{clipboard_manager}}`
