# aplay

> Command-line sound player for ALSA soundcard driver.
> More information: <https://manned.org/aplay>.

- Play a specific file (sampling rate, bit depth, etc. will be automatically determined for the file format):

`aplay {{path/to/file}}`

- Play the first 10 seconds of a specific file at 2500Hz:

`aplay --duration={{10}} --rate={{2500}} {{path/to/file}}`

- Play the raw file as a 22050Hz, mono, 8-bit, Mu-Law `.au` file:

`aplay --channels={{1}} --file-type {{raw}} --rate={{22050}} --format={{mu_law}} {{path/to/file}}`
