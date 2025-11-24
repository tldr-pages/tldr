# wacaw

> Capture both still pictures and video from an attached camera.
> More information: <https://webcam-tools.sourceforge.net/#parameters>.

- Take a picture from webcam:

`wacaw {{filename}}`

- Record a video:

`wacaw --video {{filename}} {{[-D|--duration]}} {{10}}`

- Take a picture with custom resolution:

`wacaw {{[-x|--width]}} {{width}} {{[-y|--height]}} {{100}} {{filename}}`

- Copy image just taken to clipboard:

`wacaw --to-clipboard`

- List the devices available:

`wacaw {{[-L|--list-devices]}}`
