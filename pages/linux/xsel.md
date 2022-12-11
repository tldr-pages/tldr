# xsel

> X11 selection and clipboard manipulation tool.
> More information: <https://manned.org/xsel>.

- Use a command's output as input of the clip[b]oard (equivalent to `Ctrl + C`):

`echo 123 | xsel -ib`

- Use the contents of a file as input of the clipboard:

`cat {{path/to/file}} | xsel -ib`

- Output the clipboard's contents into the terminal (equivalent to `Ctrl + V`):

`xsel -ob`

- Output the clipboard's contents into a file:

`xsel -ob > {{path/to/file}}`

- Clear the clipboard:

`xsel -cb`

- Output the X11 primary selection's contents into the terminal (equivalent to a mouse middle-click):

`xsel -op`
