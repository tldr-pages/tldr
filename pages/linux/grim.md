# grim

> Grab images (screenshots) from a Wayland compositor.
> By default, files are saved to `$GRIM_DEFAULT_DIR` or `$XDG_PICTURES_DIR` if the first variable is unset.
> If none of the environment variables are set, files are saved to the current working directory.
> More information: <https://manned.org/grim>.

- Screenshot all outputs to the default path:

`grim`

- Screenshot a specific output to the specified file:

`grim -o {{DP-1}} {{path/to/output.png}}`

- Select a specific region using `slurp` and screenshot it:

`grim -g "$(slurp)" {{path/to/output.png}}`

- Screenshot and copy the image to the clipboard:

`grim - | {{clipboard_manager}}`

- Set the output file type (default: `png`):

`grim -t {{png|ppm|jpeg}} {{path/to/output_file}}`

- Set the PNG compression level (default: 6):

`grim -l {{0-9}} {{path/to/output.png}}`

- Set the JPEG quality level (default: 80):

`grim -t jpeg -q {{0-100}} {{path/to/output.jpg}}`

- Include cursors in the screenshot:

`grim -c`
