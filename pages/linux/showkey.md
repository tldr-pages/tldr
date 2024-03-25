# showkey

> Display the keycode of pressed keys on the keyboard, helpful for debugging keyboard-related issues and key remapping.
> More information: <https://man7.org/linux/man-pages/man1/showkey.1.html>.

- View keycodes in decimal:

`sudo showkey`

- Display [s]cancodes in hexadecimal:

`sudo showkey {{-s|--scancodes}}`

- Display [k]eycodes in decimal (default):

`sudo showkey {{-k|--keycodes}}`

- Display keycodes in [a]SCII, decimal, and hexadecimal:

`sudo showkey {{-a|--ascii}}`

- Exit the program:

`Ctrl + d`
