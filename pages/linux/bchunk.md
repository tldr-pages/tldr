# bchunk

> Command-line tool for converting .bin files to .iso files.
> More information: <http://he.fi/bchunk>.

- Convert binary CD into a standard iso9960 image file:

`bchunk {{image.bin}} {{image.cue}} {{output}}`

- Convert with verbose mode:

`bchunk -v {{image.bin}} {{image.cue}} {{output}}`

- Output audio files in WAV format:

`bchunk -w {{file.bin}} {{image.cue}} {{output}}`
