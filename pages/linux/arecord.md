# arecord

> Sound recorder for ALSA soundcard driver.

- Record a snippet in "CD" quality:

`arecord -vv -f cd output.wav`

- Pass a raw recording for further processing:

`arecord -v -f cd -t raw | lame -r - output.mp3`
