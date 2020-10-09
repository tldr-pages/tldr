# aplay

> Command-line sound player for ALSA soundcard driver.

- Play file "foobar". Sampling rate, bit depth, and so forth will be automatically determined for supported soundfile formats:

`aplay {{foobar}}`

- Play first 10 seconds of soundfile at 2500hz

`aplay -d 10 -r 2500 foobar`

- Play the raw file "foobar" as a 22050-Hz, mono, 8-bit, Mu-Law .au file:

`aplay -c 1 -t raw -r 22050 -f mu_law {{foobar}}`
