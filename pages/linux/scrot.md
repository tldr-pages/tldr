# scrot

> Screen capture utility.
> More information: <https://github.com/resurrecting-open-source-projects/scrot>.

- Capture a screenshot and save it to the current directory with the current date as the filename:

`scrot`

- Capture a screenshot and save it as `capture.png`:

`scrot {{capture.png}}`

- Capture a screenshot interactively:

`scrot --select`

- Capture a screenshot interactively without exiting on keyboard input, press `ESC` to exit:

`scrot --select --ignorekeyboard`

- Capture a screenshot interactively delimiting the region with a colored line:

`scrot --select --line color={{x11_color|rgb_color}}`

- Capture a screenshot from the currently focused window:

`scrot --focused`

- Display a countdown of 10 seconds before taking a screenshot:

`scrot --count --delay {{10}}`
