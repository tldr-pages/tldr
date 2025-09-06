# maim

> Screenshot utility.
> More information: <https://manned.org/maim>.

- Capture a screenshot and save it to the given path:

`maim {{path/to/screenshot.png}}`

- Capture a screenshot of the selected region:

`maim {{[-s|--select]}} {{path/to/screenshot.png}}`

- Capture a screenshot of the selected region and save it in the clipboard (requires `xclip`):

`maim {{[-s|--select]}} | xclip {{[-se|-selection]}} {{[c|clipboard]}} {{[-t|-target]}} image/png`

- Capture a screenshot of the current active window (requires `xdotool`):

`maim {{[-i|--window]}} $(xdotool getactivewindow) {{path/to/screenshot.png}}`
