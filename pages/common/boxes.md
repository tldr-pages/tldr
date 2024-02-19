# boxes

> Draw, remove, and repair ASCII art boxes.
> More information: <https://boxes.thomasjensen.com/boxes-man-1.html>.

- Draw a box around a string:

`echo "{{string}}" | boxes`

- [r]emove a box from a string:

`echo "{{string}}" | boxes -r`

- Specify the box [d]esign:

`echo "{{string}}" | boxes -d {{parchment}}`

- Specify the box [s]ize (in columns by lines):

`echo "{{string}}" | boxes -s {{10}}x{{5}}`

- [a]lign the box text [h]orizonally (at [l]eft, [c]enter or [r]ight):

`echo "{{string}}" | boxes -a h{{l|c|r}}`

- [a]lign the box text [v]ertically (at [t]op, [c]enter or [b]ottom):

`echo "{{string}}" | boxes -a v{{t|c|b}}`

- [j]ustify the box text (at [l]eft, [c]enter or [r]ight):

`echo "{{string}}" | boxes -a j{{l|c|r}}{{vt}}`
