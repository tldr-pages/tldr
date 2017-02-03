# import

> Capture some or all of an X server screen and save the image to a file.
> Part of ImageMagick library.

- Capture the entire X server screen in the Postscript image format:

`import -window root {{output.postscript}}`

- Capture contents of remote x server screen in the `png` image format:

`import -window root -display {{remote_host}}:{screen}.{display} {{output.png}}`

- Capture specific window with ID as displayed by `xwininfo` into `jpg` format:

`import -window {{window_id}} {{output.jpg}}`
