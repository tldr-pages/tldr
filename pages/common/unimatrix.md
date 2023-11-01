# unimatrix

> A script to simulate the "Matrix" look with unicode characters.
> See also: `cmatrix`.
> More information: <https://github.com/will8211/unimatrix>.

- Mimic the default output of `cmatrix` (no unicode, works in TTY):

`unimatrix --no-bold --speed={{96}} --character-list={{o}}`

- No bold characters, slowly, with emojis, numbers, and a few symbols:

`unimatrix --no-bold --character-list={{ens}} --speed={{50}}`

- Change color or characters:

`unimatrix -c {{COLOR}}`

- Select character set(s) using a string over letter codes:

`unimatrix --character-list={{CHARACTER_SET}}`

- Change scrolling speed:

`unimatrix --speed={{SPEED}}`
