# aplay

> Sound player for ALSA soundcard driver.
> More information: <https://manned.org/aplay>.

- Play a specific file (sampling rate, bit depth, etc. will be automatically determined for the file format):

`aplay {{path/to/file}}`

- Play the first 10 seconds of a specific file at 2500 Hz:

`aplay {{[-d|--duration]}} {{10}} {{[-r|--rate]}} {{2500}} {{path/to/file}}`

- Play the raw file as a 22050 Hz, mono, 8-bit, Mu-Law `.au` file:

`aplay {{[-c|--channels]}} {{1}} {{[-t|--file-type]}} {{raw}} {{[-r|--rate]}} {{22050}} {{[-f|--format]}} {{mu_law}} {{path/to/file}}`

- List available audio devices:

`aplay {{[-l|--list-devices]}}`
