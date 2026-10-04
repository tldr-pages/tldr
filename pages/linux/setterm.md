# setterm

> Set terminal attributes such as colors, cursor visibility and screen blanking.
> Some options only work in a Linux virtual console.
> More information: <https://manned.org/setterm>.

- Clear the screen:

`setterm --clear`

- Make the cursor visible or invisible:

`setterm --cursor {{on|off}}`

- Turn blinking text on or off:

`setterm --blink {{on|off}}`

- Set the text color:

`setterm --foreground {{red}}`

- Set the background color:

`setterm --background {{black}}`

- Blank the screen after a number of minutes of inactivity (`0` disables blanking):

`setterm --blank {{10}}`

- Reset the terminal to its default state:

`setterm --reset`
