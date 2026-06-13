# xwininfo

> Display information about windows.
> See also: `xprop`, `xkill`.
> More information: <https://www.x.org/releases/current/doc/man/man1/xwininfo.1.xhtml>.

- Display a cursor to select a window to display its attributes (id, name, size, position, ...):

`xwininfo`

- Display the tree of all windows:

`xwininfo -tree -root`

- Display the attributes of a window with a specific ID:

`xwininfo -id {{id}}`

- Display the attributes of a window with a specific name:

`xwininfo -name {{name}}`

- Display the ID of a window searching by name:

`xwininfo -tree -root | grep {{keyword}} | head -1 | perl -ne 'print $1 if /(0x[\da-f]+)/ig;'`
