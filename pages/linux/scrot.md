# scrot

> Screen capture utility.
> More information: <https://manned.org/scrot>.

- Capture a screenshot and save it to the current directory with the current date as the filename:

`scrot`

- Capture a screenshot and save it as `capture.png`:

`scrot capture.png`

- Capture a screenshot interactively:

`scrot {{[-s|--select]}}`

- Capture a screenshot interactively without exiting on keyboard input, press `<Esc>` to exit:

`scrot {{[-is|--ignorekeyboard --select]}}`

- Capture a screenshot interactively delimiting the region with a colored line:

`scrot {{[-s|--select]}} {{[-l|--line]}} color={{x11_color|rgb_color}}`

- Capture a screenshot from the currently focused window:

`scrot {{[-u|--focused]}}`

- Display a countdown of 10 seconds before taking a screenshot:

`scrot {{[-c|--count]}} {{[-d|--delay]}} 10`
