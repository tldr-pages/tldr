# tty-clock

> A customizable terminal-based digital clock.
> More information: <https://github.com/xorg62/tty-clock>.

- Start the clock in the center of the terminal:

`tty-clock -c`

- Enable the display of seconds:

`tty-clock -s`

- Set the color of the clock using a color code (0-7):

`tty-clock -C {{color_number}}`

- Use a custom date format (strftime format):

`tty-clock -f "{{%A, %B %d}}"`

- Set a custom refresh delay in seconds (default is 1):

`tty-clock -d {{seconds}}`

- Exit the clock (while running):

`<q>`
