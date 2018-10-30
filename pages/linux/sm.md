# sm

> Displays a short text fullscreen.

- Display a text fullscreen:

`sm {{Hello World!}}`

- Display a text with inverted colors:

`sm -i {{Hello World!}}`

- Display a text with a foreground color:

`sm -f {{blue}} {{Hello World!}}`

- Display a text with a background color:

`sm -b {{#008888}} {{Hello World!}}`

- Rotate the displayed text by n times 90 degrees:

`sm -r {{3}} {{Hello World!}}`

- Pipe text to sm:

`{{echo Hello World!}} | sm -`
