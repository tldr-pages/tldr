# maim

> Screenshot utility

- Capture a screenshot and save it as "path/to/screenshot.png"

`maim path/to/screenshot.png`

- Capture a screenshot of the selected region

`maim -s path/to/screenshot.png`

- Capture a screenshot of the selected region and save it in the clipboard(requires xclip)

`maim -s | xclip -selection clipboard -t image/png`

- Capture a screenshot of the current active window

`maim -i $(xdotool getactivewindow) path/to/screenshot.png`
