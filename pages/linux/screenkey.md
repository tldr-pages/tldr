# screenkey

> A screencast tool to display your keys.
> More information: <https://www.thregr.org/~wavexx/software/screenkey/>.

- Display your keys pressed on the screen:

`screenkey`

- Display your keys and mouse buttons pressed on the screen:

`screenkey --mouse`

- Launch settings menu of screenkey:

`screenkey --show-settings`

- Change the position of screenkey:

`screenkey --position {{top|center|bottom|fixed}}`

- Change the format of the key modifiers displayed on screen:

`screenkey --mods-mode {{normal|emacs|mac|win|tux}}`

- Change the appearance of screenkey:

`screenkey --bg-color "{{#353535}}" --font {{Hack}} --font-color {{yellow}} --opacity {{0.8}}`

- Drag and select a window on screen to display screenkey:

`screenkey --position fixed --geometry {{$(slop -n -f '%g')}}`
