# import

> Capture some or all of an X server screen, and save the image to a file.
> Part of ImageMagick.
> More information: <https://imagemagick.org/script/import.php>.

- Capture the entire X server screen into a PostScript file:

`import -window root {{path/to/output.ps}}`

- Capture contents of a remote X server screen into a PNG image:

`import -window root -display {{remote_host}}:{{screen}}.{{display}} {{path/to/output.png}}`

- Capture a specific window given its ID as displayed by `xwininfo` into a JPEG image:

`import -window {{window_id}} {{path/to/output.jpg}}`
