# import

> Capture some or all of an X server screen, and save the image to a file.
> Part of the ImageMagick library.
> More information: <https://imagemagick.org/script/import.php>.

- Capture the entire X server screen in the PostScript image format:

`import -window root {{output.postscript}}`

- Capture contents of a remote X server screen in the PNG format:

`import -window root -display {{remote_host}}:{{screen}}.{{display}} {{output.png}}`

- Capture a specific window, given its ID as displayed by `xwininfo`, into the JPEG format:

`import -window {{window_id}} {{output.jpg}}`
