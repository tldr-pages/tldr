# xclip

> X11 clipboard manipulation tool, similar to `xsel`.
> Handles the X primary and secondary selections, plus the system clipboard (`<Ctrl c>`/`<Ctrl v>`).
> See also: `wl-copy`.
> More information: <https://manned.org/xclip>.

- Copy the output from a command to the X11 primary selection area (clipboard):

`echo 123 | xclip`

- Copy the output from a command to a given X11 selection area:

`echo 123 | xclip {{[-se|-selection]}} {{primary|secondary|clipboard}}`

- Copy the output from a command to the system clipboard, using short notation:

`echo 123 | xclip {{[-se|-selection]}} {{[c|clipboard]}}`

- Copy the contents of a file into the system clipboard:

`xclip {{[-se|-selection]}} {{[c|clipboard]}} {{input_file.txt}}`

- Copy the contents of a PNG into the system clipboard (can be pasted in other programs correctly):

`xclip {{[-se|-selection]}} {{[c|clipboard]}} {{[-t|-target]}} image/png {{input_file.png}}`

- Copy the user input in the console into the system clipboard:

`xclip {{[-i|-in]}}`

- Paste the contents of the X11 primary selection area to the console:

`xclip {{[-o|-out]}}`

- Paste the contents of the system clipboard to the console:

`xclip {{[-o|-out]}} {{[-se|-selection]}} {{[c|clipboard]}}`
