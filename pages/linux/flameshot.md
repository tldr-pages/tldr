# flameshot

> Screenshot utility with a GUI.
> Supports basic image editing, such as text, shapes, colors, and imgur.
> More information: <https://flameshot.org>.

- Launch flameshot with a simpler interactive mode:

`flameshot launcher`

- Launch flameshot and immediately start interactively annotating parts of the screen to screenshot:

`flameshot gui`

- Take a full screenshot (all monitors):

`flameshot full`

- Take a screenshot from monitor 1:

`flameshot screen --number {{1}}`

- Set the save path to write screenshots to:

`flameshot full --path {{path/to/directory}}`

- Delay the screenshot for N milliseconds and output to clipboard:

`flameshot full --delay {{2000}} --clipboard`

- Take a screenshot and export it to standard-output:

`flameshot gui --raw`
