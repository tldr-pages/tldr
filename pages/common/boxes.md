# boxes

> Draw, remove, and repair ASCII art boxes.
> More information: <https://boxes.thomasjensen.com/boxes-man-1.html>.

- Draw a box around a string:

`echo "{{string}}" | boxes`

- Remove a box from a string:

`echo "{{string}}" | boxes -r`

- Draw a box with a specific design around a string:

`echo "{{string}}" | boxes -d {{parchment}}`

- Draw a box with a width of 10 and a height of 5:

`echo "{{string}}" | boxes -s {{10}}x{{5}}`

- Draw a box with centered text:

`echo "{{string}}" | boxes -a c`
