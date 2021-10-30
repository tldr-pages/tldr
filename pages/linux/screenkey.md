# screenkey

> A screencast tool to display keys pressed.
> More information: <https://www.thregr.org/~wavexx/software/screenkey/>.

- Display keys which are currently being pressed on the screen:

`screenkey`

- Display keys and mouse buttons which are currently being pressed on the screen:

`screenkey --mouse`

- Launch the settings menu of screenkey:

`screenkey --show-settings`

- Launch screenkey at a specific position:

`screenkey --position {{top|center|bottom|fixed}}`

- Change the format of the key modifiers displayed on screen:

`screenkey --mods-mode {{normal|emacs|mac|win|tux}}`

- Change the appearance of screenkey:

`screenkey --bg-color "{{#a1b2c3}}" --font {{Hack}} --font-color {{yellow}} --opacity {{0.8}}`

- Drag and select a window on screen to display screenkey:

`screenkey --position fixed --geometry {{$(slop -n -f '%g')}}`
