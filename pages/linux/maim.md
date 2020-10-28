# maim

> Screenshot utility.
> More information: <https://github.com/naelstrof/maim>.

- Capture a screenshot and save it to the given path:

`maim {{path/to/screenshot.png}}`

- Capture a screenshot of the selected region:

`maim --select {{path/to/screenshot.png}}`

- Capture a screenshot of the selected region and save it in the clipboard (requires `xclip`):

`maim --select | xclip -selection clipboard -target image/png`

- Capture a screenshot of the current active window (requires `xdotool`):

`maim --window $(xdotool getactivewindow) {{path/to/screenshot.png}}`
