# unimatrix

> A script to simulate the "Matrix" look with unicode characters.
> See also: `cmatrix`.
> More information: <https://github.com/will8211/unimatrix>.

- Mimic default output of cmatrix (no unicode, works in TTY):

`unimatrix --no-bold --speed={{96}} --character-list={{o}}`

- No bold characters, slowly, with emojis, numbers, and a few symbols:

`unimatrix -n -l ens -s 50`

- Change color or characters:

`unimatrix -c {{COLOR}}`

- Select chracter set(s) using a string over letter codes:

`unimatrix -l {{CHARACTER_SET}}`

- Change scrolling speed:

`unimatrix -s {{SPEED}}`
