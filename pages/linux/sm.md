# sm

> Display a short message fullscreen.
> More information: <https://github.com/nomeata/screen-message>.

- Display a message in full-screen:

`sm "{{Hello World!}}"`

- Display a message with inverted colors:

`sm {{[-i|--invert]}} "{{Hello World!}}"`

- Display a message with a custom foreground color:

`sm {{[-f|--foreground]}} {{blue}} "{{Hello World!}}"`

- Display a message with a custom background color:

`sm {{[-b|--background]}} {{#008888}} "{{Hello World!}}"`

- Display a message rotated 3 times (in steps of 90 degrees, counterclockwise):

`sm {{[-r|--rotate]}} {{3}} "{{Hello World!}}"`

- Display a message using the output from another command:

`{{echo "Hello World!"}} | sm -`
