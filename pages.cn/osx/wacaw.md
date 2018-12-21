# wacaw

> A little command-line tool for macOS that allows you to capture both still pictures and video from an attached camera.

- Take a picture from webcam:

`wacaw {{filename}}`

- Record a video:

`wacaw --video {{filename}} -D {{duration_in_seconds}}`

- Take a picture with custom resolution:

`wacaw -x {{width}} -y {{height}} {{filename}}`

- Copy image just taken to clipboard:

`wacaw --to-clipboard`

- List the devices available:

`wacaw -L`
