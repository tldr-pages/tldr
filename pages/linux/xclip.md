# xclip

> X11 clipboard manipulation tool, similar to `xsel`.
> Handles the X primary and secondary selections, plus the system clipboard (`Ctrl + C`/`Ctrl + V`).

- Copy the output from a command to the X11 primary selection area (clipboard):

`echo 123 | xclip`

- Copy the output from a command to a given X11 selection area:

`echo 123 | xclip -selection {{primary|secondary|clipboard}}`

- Copy the output from a command to the system clipboard, using short notation:

`echo 123 | xclip -sel clip`

- Copy the contents of a file into the system clipboard:

`xclip -sel clip {{input_file.txt}}`

- Copy the contents of a PNG image into the system clipboard (can be pasted in other programs correctly):

`xclip -sel clip -t image/png {{input_file.png}}`

- Copy the user input in the console into the system clipboard:

`xclip -i`

- Paste the contents of the X11 primary selection area to the console:

`xclip -o`

- Paste the contents of the system clipboard to the console:

`xclip -o -sel clip`
