# farge

> Display the color of a specific pixel on the screen in either hexadecimal or RGB formats.
> More information: <https://github.com/sdushantha/farge>.

- Select a pixel interactively and display a small, square preview window of the color and it's hexadecimal value:

`farge`

- Select a pixel interactively and display a small, square preview window of the color, without displaying it's hexadecimal value:

`farge --no-color-code`

- Select a pixel interactively and output it's hexadecimal value to `stdout`:

`farge --stdout`

- Select a pixel interactively and output it's RGB value to `stdout`:

`farge --rgb --stdout`

- Select a pixel interactively and display it's hexadecimal value as a notification which expires in 5000 milliseconds:

`farge --notify --expire-time 5000`
