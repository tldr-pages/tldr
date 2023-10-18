# bchunk

> Convert CD images to a set of `.iso` and `.cdr` tracks.
> More information: <http://he.fi/bchunk>.

- Convert binary CD into a standard iso9960 image file:

`bchunk {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`

- Convert with verbose mode:

`bchunk -v {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`

- Output audio files in WAV format:

`bchunk -w {{path/to/image.bin}} {{path/to/image.cue}} {{path/to/output}}`
