# xteddy

> A cute teddy bear for your X desktop.
> More Information: <https://manned.org/xteddy.1>.

- Display a cuddly teddy bear on your X desktop:

`xteddy`

- Use the window manager to display the teddy and ignore the "quit" (`q`) command:

`xteddy -wm -noquit`

- Make the teddy stay on top of all other windows:

`xteddy -float`

- Display another image [F]ile instead of the cuddly teddy bear:

`xteddy -F {{path/to/image}}`

- Set the initial location of the teddy (`width` and `height` are ignored):

`xteddy -geometry {{width}}x{{height}}+{{x}}+{{y}}`
