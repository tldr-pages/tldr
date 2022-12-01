# wacaw

> Command-line tool for macOS to capture both still pictures and video from an attached camera.
> More information: <http://webcam-tools.sourceforge.net>.

- Take a picture from webcam:

`wacaw {{path/to/file}}`

- Record a video:

`wacaw --video {{path/to/file}} --duration {{duration_in_seconds}}`

- Take a picture with custom resolution:

`wacaw --width {{width}} --height {{height}} {{path/to/file}}`

- Copy image just taken to clipboard:

`wacaw --to-clipboard`

- List the devices available:

`wacaw --list-devices`
