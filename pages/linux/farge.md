# farge

> Display the color of a specific pixel on the screen in either hexadecimal or RGB formats.
> More information: <https://github.com/sdushantha/farge>.

- Display a small preview window of a pixel's color with it's hexadecimal value, and copy this value to the clipboard:

`farge`

- Copy a pixel's hexadecimal value to the clipboard without displaying a preview window:

`farge --no-preview`

- Output a pixel's hexadecimal value to `stdout`, and copy this value to the clipboard:

`farge --stdout`

- Output a pixel's RGB value to `stdout`, and copy this value to the clipboard:

`farge --rgb --stdout`

- Display a pixel's hexadecimal value as a notification which expires in 5000 milliseconds, and copy this value to the clipboard:

`farge --notify --expire-time 5000`
