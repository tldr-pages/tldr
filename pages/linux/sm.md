# sm

> Displays a short message fullscreen.

- Display a message fullscreen:

`sm {{Hello World!}}`

- Display a message with inverted colors:

`sm -i {{Hello World!}}`

- Display a message with a foreground color:

`sm -f {{blue}} {{Hello World!}}`

- Display a message with a background color:

`sm -b {{#008888}} {{Hello World!}}`

- Rotate the displayed message by n times 90 degrees:

`sm -r {{3}} {{Hello World!}}`

- Pipe a message to sm:

`{{echo Hello World!}} | sm -`
