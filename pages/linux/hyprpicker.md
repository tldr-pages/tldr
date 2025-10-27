# hyprpicker

> Minimal Wayland color picker for wlroots compositors (e.g., Hyprland).
> Requires a Wayland session. For clipboard autocopy, `wl-copy` must be installed.
> More information: <https://wiki.hypr.land/Hypr-Ecosystem/hyprpicker/>.

- Pick a color in the default (hex) format:

`hyprpicker`

- Pick a color and output in a specific format:

`hyprpicker {{[-f|--format]}} {{hex|rgb|hsl|hsv|cmyk}}`

- Copy the picked color to the clipboard:

`hyprpicker -a`

- Disable colored output (print plain text only):

`hyprpicker {{[-n|--no-fancy]}}`

- Use long options for format and autocopy:

`hyprpicker {{[-f|--format]}} {{rgb}} {{[-a|--autocopy]}}`

- Store the picked color in a shell variable:

`{{color}}=$(hyprpicker -f {{hex}})`

- Display help:

`hyprpicker -h`
