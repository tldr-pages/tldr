# xsel

> X11 selection and clipboard manipulation tool.
> More information: <https://manned.org/xsel>.

- Use a command's output as input of the clipboard (equivalent to `<Ctrl c>`):

`echo 123 | xsel {{[-ib|--input --clipboard]}}`

- Use the contents of a file as input of the clipboard:

`cat {{path/to/file}} | xsel {{[-ib|--input --clipboard]}}`

- Output the clipboard's contents into the terminal (equivalent to `<Ctrl v>`):

`xsel {{[-ob|--output --clipboard]}}`

- Output the clipboard's contents into a file:

`xsel {{[-ob|--output --clipboard]}} > {{path/to/file}}`

- Clear the clipboard:

`xsel {{[-cb|--clear --clipboard]}}`

- Output the X11 primary selection's contents into the terminal (equivalent to a mouse `<MiddleClick>`):

`xsel {{[-op|--output --primary]}}`
