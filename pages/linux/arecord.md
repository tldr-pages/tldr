# arecord

> Sound recorder for ALSA soundcard driver.
> More information: <https://linux.die.net/man/1/arecord>.

- Record a snippet in "CD" quality (finish with Ctrl-C when done):

`arecord -vv --format=cd {{path/to/file.wav}}`

- Record a snippet in "CD" quality, with a fixed duration of 10 seconds:

`arecord -vv --format=cd --duration={{10}} {{path/to/file.wav}}`

- Record a snippet and save it as mp3 (finish with Ctrl-C when done):

`arecord -vv --format=cd --file-type raw | lame -r - {{path/to/file.mp3}}`
