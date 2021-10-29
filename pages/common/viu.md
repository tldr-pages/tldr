# viu

> A small command-line application to view images from the terminal.
> More information: <https://github.com/atanunq/viu>.

- Render image or GIF:

`viu {{filename}}`

- Render image or GIF from the internet with help of `curl`:

`curl -s {{https://example.com/image.png}} | viu -`

- Render transparent image with transparent background:

`viu -t {{filename}}`

- Render image with specific width and height:

`viu -w {{width}} -h {{height}} {{filename}}`

- Render PNG and GIF files alongside their names:

`viu -n {{*.{png,gif}}}`
