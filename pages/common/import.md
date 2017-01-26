# import

> Capture some or all of an X server desktop screen and save the image to a file. This command is part of the ImageMagick library.

- Capture the entire X server screen in the Postscript image format:

`import -window root {{filename.postscript}}`

- Capture contents of remote x server screen in the png image format:

`import -window root -display {{remote.host}}:0.0 {{output.png}}`

- Capture specific window with ID as displayed by `xwininfo`:

`import -window {{window_id}} {{output.jpg}}
