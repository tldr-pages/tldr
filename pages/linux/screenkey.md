# screenkey

> A screencast tool to display keys pressed.
> More information: <https://www.thregr.org/~wavexx/software/screenkey/>.

- Display keys which are currently being pressed on the screen:

`screenkey`

- Display keys and mouse buttons which are currently being pressed on the screen:

`screenkey {{[-M|--mouse]}}`

- Launch the settings menu of screenkey:

`screenkey --show-settings`

- Launch screenkey at a specific position:

`screenkey {{[-p|--position]}} {{top|center|bottom|fixed}}`

- Change the format of the key modifiers displayed on screen:

`screenkey --mods-mode {{normal|emacs|mac|win|tux}}`

- Change the appearance of screenkey:

`screenkey --bg-color "{{#a1b2c3}}" {{[-f|--font]}} {{Hack}} --font-color {{yellow}} --opacity {{0.8}}`

- Drag and select a window on screen to display screenkey:

`screenkey {{[-p|--position]}} fixed {{[-g|--geometry]}} {{$(slop {{[-n|--nodecorations]}} {{[-f|--format]}} '%g')}}`
