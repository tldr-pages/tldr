# boxes

> Draw, remove, and repair ASCII art boxes.
> More information: <https://boxes.thomasjensen.com/boxes-man-1.html>.

- Draw a box around a string:

`echo "{{string}}" | boxes`

- Remove a box from a string:

`echo "{{string}}" | boxes {{[-r|--remove]}}`

- Specify the box design:

`echo "{{string}}" | boxes {{[-d|--design]}} {{parchment}}`

- Specify the box size (in columns by lines):

`echo "{{string}}" | boxes {{[-s|--size]}} {{10}}x{{5}}`

- Align the box text [h]orizonally (at [l]eft, [c]enter or [r]ight):

`echo "{{string}}" | boxes {{[-a|--align]}} h{{l|c|r}}`

- Align the box text [v]ertically (at [t]op, [c]enter or [b]ottom):

`echo "{{string}}" | boxes {{[-a|--align]}} v{{t|c|b}}`

- [j]ustify the box text (at [l]eft, [c]enter or [r]ight):

`echo "{{string}}" | boxes {{[-a|--align]}} j{{l|c|r}}{{vt}}`
